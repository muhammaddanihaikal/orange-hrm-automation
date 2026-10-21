# 🍊 OrangeHRM Automation Testing Framework

Framework otomatisasi pengujian berbasis web (End-to-End) untuk aplikasi **OrangeHRM Open Source** menggunakan **Python**, **Playwright**, dan **Pytest** dengan pola arsitektur **Page Object Model (POM)**.

---

## 🛠️ Tech Stack

* **Bahasa:** Python ≥ 3.14
* **Browser Automation:** [Playwright](https://playwright.dev/python/) (Sync API)
* **Test Runner:** [Pytest](https://docs.pytest.org/)
* **Package Manager:** [uv](https://docs.astral.sh/uv/) (Astral)
* **Reporting:** [Allure Report](https://allurereport.org/) (`allure-pytest`)
* **Environment:** Docker & Docker Compose (Local OrangeHRM + MariaDB)

---

## 🏗️ Pola & Arsitektur Pengujian

1. **Page Object Model (POM):**  
   Seluruh interaksi dan selector elemen diisolasi ke dalam class terpisah di folder `pages/` (`LoginPage`, `AdminPage`, `Sidebar`, dll.) sehingga test case hanya fokus pada alur bisnis.
2. **Pola AAA (Arrange, Act, Assert):**  
   Setiap test case menstrukturkan langkahnya secara disiplin: Persiapan (*Arrange*), Aksi (*Act*), dan Validasi (*Assert*).
3. **Session Authentication Reuse (`storage_state`):**  
   Login hanya dilakukan 1x di awal sesi pengujian via fixture `global_login`. Cookies sesi disimpan ke `.auth/state.json` dan dimuat ulang oleh fixture `logged_in_page`, memangkas durasi eksekusi pengujian secara drastis.
4. **Hybrid API Data Seeding & Teardown:**  
   Data uji pengguna disiapkan langsung melalui REST API OrangeHRM (`page.request.post`) sebelum test berjalan dan otomatis dihapus saat teardown (`delete`), menjaga pengujian tetap 100% mandiri (*self-contained*).
5. **Dynamic Synchronization:**  
   Bebas dari *static sleep* (`time.sleep`). Memanfaatkan *auto-waiting*, `page.expect_response()`, dan *web-first assertions* Playwright untuk mencegah *flakiness*.

---

## 🚀 Panduan Memulai (Quick Start)

### 1. Prasyarat
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) sudah terpasang dan berjalan.
* [uv](https://docs.astral.sh/uv/) sudah terpasang di sistem.

### 2. Menjalankan Aplikasi Web (OrangeHRM Docker)
Nyalakan container OrangeHRM dan MariaDB secara lokal:
```bash
docker compose up -d
```
> Aplikasi web akan dapat diakses di browser melalui: **`http://localhost:8080`**

### 3. Setup Lingkungan & Dependensi
Sinkronkan virtual environment dan library proyek menggunakan `uv`:
```bash
# Install seluruh library dari pyproject.toml
uv sync

# Unduh binary browser Chromium Playwright (cukup 1x di awal)
uv run playwright install
```

---

## 🧪 Menjalankan Pengujian

### Menjalankan Seluruh Test Suite:
```bash
uv run pytest
```

### Menjalankan File Test Tertentu:
```bash
# Menjalankan pengujian autentikasi
uv run pytest tests/test_login.py

# Menjalankan pengujian manajemen pengguna
uv run pytest tests/test_user.py
```

### Menjalankan Mode Debug Interaktif (Playwright Inspector):
```bash
PWDEBUG=1 uv run pytest -s tests/test_user.py -k test_reset_filter
```

---

## 📊 Menghasilkan Laporan (Allure Report)

1. Jalankan test sambil mengumpulkan data hasil uji:
   ```bash
   uv run pytest --alluredir=allure-results
   ```

2. Buka dashboard Allure interaktif di browser:
   ```bash
   allure serve allure-results
   ```

---

## 📁 Struktur Direktori

```text
orange-hrm-automation/
├── config.py              # Konfigurasi BASE_URL & status HEADLESS
├── conftest.py            # Fixtures Pytest (browser, storage_state, api seeding)
├── docker-compose.yml      # Konfigurasi container OrangeHRM lokal
├── pyproject.toml         # Manajemen dependensi proyek
├── README.md              # Panduan dokumentasi proyek
├── BELAJAR_PROGRESS.md    # Catatan pelacakan milestone pembelajaran
│
├── data/                  # Test data JSON terpisah
│   ├── login_data.json
│   └── user_data.json
├── pages/                 # Implementasi Page Object Model
│   ├── login_page.py
│   ├── sidebar.py
│   ├── admin/             # Halaman modul Admin & Form User
│   └── dashboard/         # Halaman modul Dashboard
├── tests/                 # Test suites (Pytest)
│   ├── test_login.py
│   └── test_user.py
├── utils/                 # Utility helper (Data Factory & File Reader)
│   ├── data_factory.py
│   └── read_data.py
└── testcase/              # Dokumentasi & spesifikasi test case manual
```
