# Crypto Baseline (v1)

- **Encryption**: AES-256-GCM
- **KDF**: PBKDF2-HMAC-SHA256, 310,000 iterations, 16-byte random salt
- **IV**: 12-byte random (unique per encryption)
- **AAD**: { pack_type, scenario_id, created_at_utc, sha256_plaintext }
- **Timestamp**: ISO-8601 UTC with 'Z'
- **Clock Skew Policy**: ±10 minutes default
- **Extensions**:
  - Scenario file extension: `.emsx`
  - Submission file extension: `.subx`

