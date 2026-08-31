# 📘 Progress Belajar Automation Testing — OrangeHRM

> **Tujuan file ini:** Mendokumentasikan progres belajar automation testing menggunakan pola **Page Object Model (POM)** di project OrangeHRM. File ini bisa diberikan ke AI agar AI paham konteks belajar dan bisa membantu lebih tepat sasaran.

---

## 🛠️ Tech Stack yang Digunakan

| Tool / Library | Versi | Peran |
|---|---|---|
| Python | ≥ 3.14 | Bahasa utama |
| Playwright | ≥ 1.62.0 | Browser automation |
| Pytest | ≥ 9.1.1 | Test runner |
| uv | — | Package & env manager |

**Target aplikasi:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com)

---

## 📁 Struktur Project

```
orange-hrm-automation/
├── config.py                  # BASE_URL & konfigurasi global (HEADLESS)
├── conftest.py                # Fixtures Pytest (playwright, browser, context, page)
├── pyproject.toml             # Dependency management
│
├── pages/                     # Page Object Model (POM)
│   ├── login_page.py          # Halaman Login
│   ├── sidebar.py             # Komponen Sidebar navigasi
│   ├── dashboard/
│   │   └── dashboard_page.py  # Halaman Dashboard
│   └── admin/
│       ├── admin_page.py      # Halaman daftar user (Admin > System Users)
│       ├── add_user_page.py   # Halaman form tambah user
│       └── edit_user_page.py  # Halaman form edit user
│
├── tests/                     # File test
│   ├── test_login.py          # Test login (versi awal)
│   ├── test_login2.py         # Test login (versi refactor dengan DashboardPage)
│   └── test_user.py           # Test CRUD user (add & edit)
│
├── utils/                     # Helper / utility functions
│   ├── read_data.py           # Baca file JSON dari folder data/
│   └── data_factory.py        # Generate data dinamis (misal: username unik)
│
├── data/                      # Test data dalam format JSON
│   ├── login_data.json        # Data login (valid & invalid)
│   └── user_data.json         # Data untuk add user & edit user
│
└── testcase/                  # Dokumentasi test case manual
    ├── tc_orangehrm.xlsx       # Test case dalam format Excel
    └── tc_template.md          # Template test case
```

---

## ✅ Konsep yang Sudah Dipelajari & Diimplementasikan

### 1. 📐 Page Object Model (POM)
- Setiap halaman di-representasikan sebagai **class Python** di folder `pages/`
- Locator elemen & action method dikumpulkan dalam satu class, bukan disebar di test
- Pages diorganisir dalam subfolder per modul (misal: `admin/`, `dashboard/`)

**Contoh implementasi:**
```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page: Page):
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

---

### 2. 🔧 Pytest Fixtures (`conftest.py`)
- Memahami **scope fixture**: `session`, `function`
- Fixture disusun berjenjang: `playwright` → `browser` → `context` → `page`
- Setiap test function otomatis mendapatkan `page` yang fresh (context baru)

```
Hierarki fixture yang sudah dipahami:
playwright  (scope=session)   → 1x selama semua test
  └── browser (scope=session) → 1x browser instance
        └── context (scope=function) → fresh per test
              └── page (scope=function) → fresh per test
```

---

### 3. 📂 Test Data Separation (JSON + utils)
- Data pengujian dipisah ke folder `data/` dalam format **JSON**
- Utility `read_data.py` membaca file JSON secara generik
- Prinsip: test file tidak hardcode data, semua dari file terpisah

**Contoh:**
```python
# utils/read_data.py
def read_data(file_name: str):
    with open(DATA_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)

# Penggunaan di test:
login_data = read_data("login_data.json")
data = login_data["valid_login"]
```

---

### 4. 🏭 Data Factory
- Membuat fungsi `generate_username()` di `utils/data_factory.py` untuk generate data dinamis
- Menggunakan `uuid` agar username selalu unik setiap kali test dijalankan
- Mencegah konflik data antar-run

```python
# utils/data_factory.py
import uuid

def generate_username(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"
    # Contoh hasil: "dani_3f2a1b4c"
```

---

### 5. 🧭 Shared Component — Sidebar
- Sidebar direpresentasikan sebagai Page Object tersendiri (`sidebar.py`)
- Digunakan di berbagai test tanpa duplikasi locator
- Konsep: komponen yang muncul di banyak halaman dibuat class sendiri

```python
# pages/sidebar.py
class Sidebar:
    def __init__(self, page: Page):
        self.admin = page.get_by_role("link", name="Admin")
        self.pim = page.get_by_role("link", name="PIM")
        # dst...
```

---

### 6. 🔍 Playwright Locator Strategy
Berbagai strategi locator yang sudah digunakan:

| Strategi | Contoh | Digunakan di |
|---|---|---|
| `get_by_role()` | `page.get_by_role("textbox", name="Username")` | Login, form fields |
| `locator()` | `page.locator(".oxd-input-group")` | Filter container class CSS |
| `.filter(has_text=)` | `.filter(has_text="User Role")` | Narrow down elemen yang mirip |
| `.filter(has=)` | `.filter(has=page.locator("i.bi-pencil-fill"))` | Filter by child element |
| `.nth()` | `.get_by_role("cell").nth(2)` | Ambil elemen berdasarkan urutan |
| `.first` | `.locator("div").first` | Ambil elemen pertama dari list |

---

### 7. ✔️ Playwright Assertion (`expect`)
Assertion yang sudah digunakan:

```python
from playwright.sync_api import expect

expect(page).to_have_url("...")           # Cek URL halaman
expect(page).to_have_title("OrangeHRM")  # Cek title halaman
expect(element).to_be_visible()          # Elemen terlihat di layar
expect(element).to_contain_text("...")   # Elemen mengandung teks
expect(element).to_have_text("...")      # Elemen memiliki teks persis
```

---

### 8. 📝 Test yang Sudah Ditulis

#### `test_login.py` — Versi awal
| Test Case | Skenario | Status |
|---|---|---|
| `test_login_success` | Login dengan kredensial valid | ✅ |
| `test_login_invalid_username` | Login dengan username salah | ✅ |
| `test_login_invalid_password` | Login dengan password salah | ✅ |
| `test_login_invalid_credentials` | Login dengan keduanya salah | ✅ |

#### `test_login2.py` — Versi refactor
Versi yang lebih bersih: menggunakan `DashboardPage` untuk assertion redirect,
dan memakai `login_page.heading` sebagai locator (bukan inline `get_by_role`).

| Test Case | Skenario | Status |
|---|---|---|
| `test_login_valid` | Login valid + verifikasi redirect ke Dashboard | ✅ |
| `test_login_invalid_username` | Login username salah (partial, belum ada assertion) | ⚠️ |
| `test_login_invalid_password` | Login password salah (partial, belum ada assertion) | ⚠️ |

#### `test_user.py` — Test CRUD user
| Test Case | Skenario | Status |
|---|---|---|
| `test_add_user` | Tambah user baru + verifikasi muncul di tabel | ✅ |
| `test_edit_user` | Edit user (role, employee, status, password) + verifikasi | ✅ |

---

## 🔄 Alur yang Sudah Dipahami untuk Test CRUD

```
test_add_user:
  login → klik sidebar "Admin" → klik "Add" →
  isi form (user_role, employee_name, status, username, password) →
  save → verifikasi redirect → search user → verifikasi row ada di tabel

test_edit_user:
  login → klik sidebar "Admin" → search user →
  klik edit button → ubah (user_role, employee, status, change_password) →
  save → verifikasi redirect → search user → verifikasi cell (role, employee, status)
```

---

## 🎯 Goals Belajar Selanjutnya (To-Do List)

- [ ] **Data-Driven Testing (DDT) dengan `@pytest.mark.parametrize`**: Mengubah test berulang (misalnya test validasi login dengan berbagai error) menjadi 1 fungsi saja.
- [ ] **Reuse Authentication State**: Menyimpan status login (cookies) ke sebuah file dan memuatnya ke fixture `logged_in_page`, supaya test CRUD tidak perlu mengulang proses login UI dari awal.
- [ ] **Network Interception & API Response**: Menggunakan `page.wait_for_response()` untuk memastikan API di background sudah membalas request, sehingga test lebih stabil (mengurangi *flakiness*).
- [ ] **Negative Test Case & Edge Cases**: Menguji validasi form (misal: membiarkan form tambah user kosong) lalu membuat assertion pada *error message* yang muncul.
- [ ] **HTML Reporting**: Mengonfigurasi `pytest-html` atau `Allure` agar hasil automation testing bisa dilihat dalam bentuk dashboard web/HTML interaktif yang rapi.

---

## 💡 Poin Penting & Pelajaran

1. **Jangan hardcode selector** di test langsung — taruh di Page Object
2. **`filter(has_text=)`** sangat berguna untuk narrow down elemen yang punya class CSS sama tapi label berbeda (seperti form fields di OrangeHRM yang semua pakai `.oxd-input-group`)
3. **Data dinamis** (seperti username) harus di-generate sekali di module level, bukan per-test, agar `test_add_user` dan `test_edit_user` pakai username yang sama
4. **`.wait_for(state="hidden")`** dan **`.wait_for(state="visible")`** penting untuk handle elemen async (seperti dropdown search yang butuh waktu load)
5. **Scope fixture `session`** untuk browser = efisiensi (tidak buka/tutup browser tiap test), tapi context & page tetap `function` scope agar test terisolasi
