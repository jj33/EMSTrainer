#!/usr/bin/env python3
"""
EMSTrainer Test Validation Script
Validates stress test results locally without AI provider limits

Usage:
    python3 scripts/validate_test_results.py
    python3 scripts/validate_test_results.py --batch tests/VF_Paramedic_Standard_Graded
"""

import json
import csv
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

class TestValidator:
    def __init__(self, test_dir: Path):
        self.test_dir = test_dir
        self.results = []
        self.expected_distribution = {
            'A': 8,  # Excellent (27-33% target)
            'B': 4,  # Good (40% target) 
            'C': 5,  # Adequate (27% target)
            'D': 13  # Poor (13% target)
        }
        
    def load_graded_results(self) -> List[Dict]:
        """Load all graded student JSON files"""
        results = []
        for json_file in sorted(self.test_dir.glob('graded_student_*.json')):
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                    results.append(data)
            except json.JSONDecodeError as e:
                print(f"❌ Error loading {json_file.name}: {e}")
            except Exception as e:
                print(f"❌ Unexpected error with {json_file.name}: {e}")
        
        return results
    
    def load_csv_scores(self) -> List[Dict]:
        """Load the graded_scores.csv file"""
        csv_path = self.test_dir / 'graded_scores.csv'
        if not csv_path.exists():
            print(f"⚠️  Warning: {csv_path} not found")
            return []
        
        scores = []
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            scores = list(reader)
        
        return scores
    
    def validate_json_structure(self, results: List[Dict]) -> Tuple[int, List[str]]:
        """Validate that all JSON files have required fields"""
        required_fields = [
            'student_id', 'scenario_id', 'scenario_hash_match',
            'scores', 'hidden_criteria', 'timings', 'outcome',
            'strengths', 'areas_for_improvement'
        ]
        
        errors = []
        valid_count = 0
        
        for result in results:
            student_id = result.get('student_id', 'unknown')
            missing = [f for f in required_fields if f not in result]
            
            if missing:
                errors.append(f"{student_id}: Missing fields {missing}")
            else:
                valid_count += 1
        
        return valid_count, errors
    
    def check_grade_distribution(self, results: List[Dict]) -> Dict:
        """Check if grade distribution matches expected"""
        actual = defaultdict(int)
        
        for result in results:
            letter_grade = result.get('scores', {}).get('letter_grade', 'X')
            actual[letter_grade] += 1
        
        comparison = {}
        for grade in ['A', 'B', 'C', 'D']:
            expected = self.expected_distribution.get(grade, 0)
            got = actual.get(grade, 0)
            diff = got - expected
            comparison[grade] = {
                'expected': expected,
                'actual': got,
                'diff': diff
            }
        
        return comparison
    
    def check_score_ranges(self, results: List[Dict]) -> Dict:
        """Validate score ranges and statistics"""
        scores = []
        
        for result in results:
            total = result.get('scores', {}).get('total', 0)
            scores.append(total)
        
        if not scores:
            return {}
        
        return {
            'min': min(scores),
            'max': max(scores),
            'mean': sum(scores) / len(scores),
            'count': len(scores)
        }
    
    def validate_hash_matches(self, results: List[Dict]) -> Tuple[int, int]:
        """Check how many submissions have matching scenario hashes"""
        matched = sum(1 for r in results if r.get('scenario_hash_match', False))
        total = len(results)
        return matched, total
    
    def check_rosc_outcomes(self, results: List[Dict]) -> Dict:
        """Analyze ROSC outcomes"""
        rosc_achieved = sum(1 for r in results if r.get('outcome', {}).get('ROSC', False))
        total = len(results)
        
        return {
            'rosc_count': rosc_achieved,
            'total': total,
            'rosc_rate': (rosc_achieved / total * 100) if total > 0 else 0
        }
    
    def compare_json_to_csv(self, json_results: List[Dict], csv_scores: List[Dict]) -> List[str]:
        """Verify JSON and CSV data match"""
        errors = []
        
        # Create lookup dict from CSV
        csv_lookup = {row['student_id']: row for row in csv_scores}
        
        for result in json_results:
            student_id = result.get('student_id')
            json_total = result.get('scores', {}).get('total', 0)
            json_grade = result.get('scores', {}).get('letter_grade', '')
            
            if student_id not in csv_lookup:
                errors.append(f"{student_id}: Not found in CSV")
                continue
            
            csv_row = csv_lookup[student_id]
            csv_total = int(csv_row.get('total', 0))
            csv_grade = csv_row.get('letter', '')
            
            if json_total != csv_total:
                errors.append(f"{student_id}: Score mismatch (JSON={json_total}, CSV={csv_total})")
            
            if json_grade != csv_grade:
                errors.append(f"{student_id}: Grade mismatch (JSON={json_grade}, CSV={csv_grade})")
        
        return errors
    
    def run_validation(self) -> bool:
        """Run all validation checks"""
        print(f"\n{'='*70}")
        print(f"EMSTrainer Test Validation Report")
        print(f"{'='*70}")
        print(f"Test Directory: {self.test_dir}")
        print()
        
        # Load data
        print("📂 Loading test data...")
        json_results = self.load_graded_results()
        csv_scores = self.load_csv_scores()
        
        if not json_results:
            print("❌ No JSON results found!")
            return False
        
        print(f"✅ Loaded {len(json_results)} JSON files")
        print(f"✅ Loaded {len(csv_scores)} CSV rows")
        print()
        
        # Validate JSON structure
        print("🔍 Validating JSON structure...")
        valid_count, structure_errors = self.validate_json_structure(json_results)
        print(f"✅ {valid_count}/{len(json_results)} files have valid structure")
        
        if structure_errors:
            print("⚠️  Structure issues found:")
            for error in structure_errors[:5]:  # Show first 5
                print(f"   - {error}")
            if len(structure_errors) > 5:
                print(f"   ... and {len(structure_errors) - 5} more")
        print()
        
        # Check grade distribution
        print("📊 Grade Distribution Analysis...")
        grade_dist = self.check_grade_distribution(json_results)
        
        print(f"{'Grade':<8} {'Expected':<12} {'Actual':<12} {'Diff':<8} {'Status'}")
        print("-" * 50)
        
        all_grades_ok = True
        for grade in ['A', 'B', 'C', 'D']:
            data = grade_dist[grade]
            diff = data['diff']
            status = '✅' if abs(diff) <= 2 else '⚠️'
            
            if abs(diff) > 2:
                all_grades_ok = False
            
            print(f"{grade:<8} {data['expected']:<12} {data['actual']:<12} "
                  f"{diff:+3d}      {status}")
        print()
        
        # Score ranges
        print("📈 Score Statistics...")
        score_stats = self.check_score_ranges(json_results)
        print(f"   Min:  {score_stats['min']}/100")
        print(f"   Max:  {score_stats['max']}/100")
        print(f"   Mean: {score_stats['mean']:.1f}/100")
        print(f"   Count: {score_stats['count']} students")
        print()
        
        # Hash validation
        print("🔐 Hash Validation...")
        matched, total = self.validate_hash_matches(json_results)
        print(f"   {matched}/{total} submissions have matching scenario hashes")
        
        if matched == total:
            print("   ✅ All hashes match!")
        else:
            print(f"   ⚠️  {total - matched} hash mismatches found")
        print()
        
        # ROSC outcomes
        print("💓 ROSC Outcomes...")
        rosc_data = self.check_rosc_outcomes(json_results)
        print(f"   {rosc_data['rosc_count']}/{rosc_data['total']} students achieved ROSC")
        print(f"   ROSC rate: {rosc_data['rosc_rate']:.1f}%")
        print()
        
        # JSON vs CSV comparison
        if csv_scores:
            print("🔀 JSON ↔ CSV Comparison...")
            comparison_errors = self.compare_json_to_csv(json_results, csv_scores)
            
            if comparison_errors:
                print(f"   ⚠️  {len(comparison_errors)} discrepancies found:")
                for error in comparison_errors[:5]:
                    print(f"      - {error}")
                if len(comparison_errors) > 5:
                    print(f"      ... and {len(comparison_errors) - 5} more")
            else:
                print("   ✅ JSON and CSV data match perfectly!")
            print()
        
        # Final verdict
        print(f"{'='*70}")
        
        all_ok = (
            len(structure_errors) == 0 and
            all_grades_ok and
            matched == total and
            (not csv_scores or len(comparison_errors) == 0)
        )
        
        if all_ok:
            print("✅ ALL VALIDATION CHECKS PASSED!")
            print("\nTest data is valid and ready for regression baseline.")
        else:
            print("⚠️  SOME VALIDATION CHECKS FAILED")
            print("\nReview issues above before using as regression baseline.")
        
        print(f"{'='*70}\n")
        
        return all_ok


def main():
    # Default test directory
    default_dir = Path('tests/VF_Paramedic_Standard_Graded')
    
    # Check for command line argument
    if len(sys.argv) > 1:
        test_dir = Path(sys.argv[1])
    else:
        test_dir = default_dir
    
    # Validate directory exists
    if not test_dir.exists():
        print(f"❌ Error: Directory not found: {test_dir}")
        print(f"\nUsage: python3 {sys.argv[0]} [test_directory]")
        print(f"Example: python3 {sys.argv[0]} tests/VF_Paramedic_Standard_Graded")
        sys.exit(1)
    
    # Run validation
    validator = TestValidator(test_dir)
    success = validator.run_validation()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
