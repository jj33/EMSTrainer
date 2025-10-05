# EMSTrainer

EMSTrainer is a structured, versioned repository of EMS training materials designed to support paramedic students, instructors, and AI-assisted study workflows. It provides clean, organized source documents, study guides, and prompts — all optimized for non-commercial educational use.

---

## 📘 What This Project Contains

- ✅ Editable source documents (`.pages`) for EMS training
- ✅ Exported assets (`.pdf`) for printing and distribution
- ✅ Versioned imports from external sources
- ✅ Cleanup tooling to normalize and organize content
- ✅ Contributor guidelines for expanding the library

---

## 🧭 How It Works

1. **Import** new materials into `docs/imports/<version>/`
2. **Run cleanup** with `scripts/cleanup-import.sh <version> --apply`
3. **Convert `.docx` to `.pages`** and move to `docs/source/`
4. **Export `.pdf`** versions to `assets/`
5. **Commit and tag** each cleaned version

See [`docs/README.md`](docs/README.md) for full documentation.

---

## 🧪 For Educators & Students

All materials are free to use for **non-commercial educational purposes**. You may:

- Copy and distribute PDFs
- Adapt source documents
- Reference or remix content in your own study guides

Each exported document includes a license badge and footer referencing this project.

---

## 🤝 Contributing

Want to add new scenarios, prompts, or guides?

- See [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Follow the versioned import and cleanup workflow
- Submit a pull request with your additions

---

## 🛠 Tooling

- `scripts/cleanup-import.sh` — organizes imported files
- `.gitignore` — filters out macOS and editor artifacts
- `docs/source/README.md` — explains how to structure source documents
- `docs/assets/README.md` — explains exported PDFs

---

## 📎 License

This project is licensed under [CC BY-NC 4.0](LICENSE). You may use and adapt materials for non-commercial educational purposes with attribution.

Badge and footer are automatically included in all future document exports.
