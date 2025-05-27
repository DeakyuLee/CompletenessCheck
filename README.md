# 🧩 Android Translation Completeness Checker

This is a simple Python tool that checks for **missing string resources** across localized `strings.xml` files in an Android project.

It compares all `res/values-*/strings.xml` files against the base `res/values/strings.xml`, and generates a report of missing translation keys per locale.

---

## 🚀 Features

- Detects missing keys and extra keys in localized `strings.xml` files
- Supports any number of locales (e.g., `values-fr`, `values-ja`)
- Outputs CSV files
- CLI-friendly — ideal for CI workflows or localization QA

---

## 📁 Directory Assumptions

Your project should follow the standard Android resource structure

## 🚀 Quick Start

### 1. **Download the Release**

- [📦 Download the latest release](https://github.com/DeakyuLee/CompletenessCheck/releases/tag/v1.0.0)
- translation_checker

---

### 2. **Prepare Your Config File**

Create a file called `config.json` in the **same folder** as the binary:

```json
{
    "resourcePath": "<project-directory>/app/src/main/res"
}
```

### 3. Update permission

run `chmod +x completeness_check`

### 4. Run the binary

run `./completeness_check`

### 5. (Optional) When running on mac

run `xattr -d com.apple.quarantine completeness_check` to override Gatekeeper warning

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.