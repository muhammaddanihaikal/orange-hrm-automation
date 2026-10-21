# 📘 Progress Belajar Automation Testing — OrangeHRM

> **Tujuan file ini:** Mendokumentasikan progres belajar automation testing menggunakan pola **Page Object Model (POM)** di project OrangeHRM. File ini bisa diberikan ke AI agar AI paham konteks belajar dan bisa membantu lebih tepat sasaran.

---

## 🛠️ Tech Stack yang Digunakan

| Tool / Library | Versi | Peran |
|---|---|---|
| Python | ≥ 3.14 | Bahasa utama |
| Playwright | ≥ 1.62.0 | Browser automation |
| Pytest | ≥ 9.1.1 | Test runner |
| Allure Pytest | ≥ 2.16.0 | Reporting framework |
| uv | — | Package & env manager |

**Target aplikasi:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com) / Local Docker (`http://localhost:8080`)

---

## 📁 Struktur Project

```
orange-hrm-automation/
├── config.py                  # BASE_URL & konfigurasi global (HEADLESS)
├── conftest.py                # Fixtures Pytest (playwright, browser, context, page, auth, api seeding)
├── pyproject.toml             # Dependency management
├── README.md                  # Dokumentasi petunjuk menjalankan pengujian
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
│   ├── test_login.py          # Test autentikasi login (DDT parametrize & validasi form)
│   └── test_user.py           # Test CRUD user & filter manajemen user (11 TC)
│
├── utils/                     # Helper / utility functions
│   ├── read_data.py           # Baca file JSON dari folder data/
│   └── data_factory.py        # Generate data dinamis (misal: username unik via UUID)
│
├── data/                      # Test data dalam format JSON
│   ├── login_data.json        # Data login (valid, invalid, empty)
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

#### `test_login.py` — Pengujian Autentikasi
| Test Case ID | Skenario | Status |
|---|---|:---:|
| `TC-AUTH-01` | Melakukan login menggunakan data yang valid | ✅ |
| `TC-AUTH-02` | Melakukan login menggunakan data yang tidak valid (DDT) | ✅ |
| `TC-AUTH-03` | Melakukan login tanpa mengisi field mandatory (DDT) | ✅ |

#### `test_user.py` — Pengujian Manajemen User (Admin > System Users)
| Test Case ID | Skenario | Status |
|---|---|:---:|
| `TC-ADMIN-01` | Menambahkan data System Users | ✅ |
| `TC-ADMIN-02` | Menambahkan data System Users tanpa mengisi field mandatory | ✅ |
| `TC-ADMIN-03` | Mengubah data System Users | ✅ |
| `TC-ADMIN-04` | Menghapus data System Users | ✅ |
| `TC-ADMIN-05` | Melakukan filter data System Users berdasarkan Username | ✅ |
| `TC-ADMIN-06` | Melakukan filter data System Users berdasarkan User Role | ✅ |
| `TC-ADMIN-07` | Melakukan filter data System Users berdasarkan Employee Name | ✅ |
| `TC-ADMIN-08` | Melakukan filter data System Users berdasarkan Status | ✅ |
| `TC-ADMIN-09` | Mereset filter System Users (Bebas Race Condition) | ✅ |
| `TC-ADMIN-10` | Melakukan filter data System Users kombinasi (Mandiri via API Fixture) | ✅ |
| `TC-ADMIN-11` | Menghapus data System Users secara massal (Bulk Delete) | ✅ |

---

## 🔄 Alur yang Sudah Dipahami untuk Test CRUD

```
test_add_user:
  login → klik sidebar "Admin" → klik "Add" →
  isi form (user_role, employee_name, status, username, password) →
  save → tunggu alert sukses → verifikasi redirect → search user → verifikasi row ada di tabel

test_edit_user:
  login → klik sidebar "Admin" → search user →
  klik edit button → ubah (user_role, employee, status, change_password) →
  save → tunggu alert sukses → verifikasi redirect → search user → verifikasi cell (role, employee, status)

test_delete_user:
  login → klik sidebar "Admin" → search user →
  delete user via Action Method (klik trash + konfirmasi popup) →
  search user lagi → verifikasi row hidden & No Records Found muncul
```

---

## 🎯 Goals Belajar yang Sudah Berhasil Dicapai (Milestones)

- [x] **Data-Driven Testing (DDT) dengan `@pytest.mark.parametrize`**: Mengubah test login berulang menjadi 1 fungsi saja dengan pemisahan validasi.
- [x] **Full CRUD Flow (Create, Read, Update, Delete)**: Menyelesaikan pengujian lengkap untuk manajemen user di `test_user.py`.
- [x] **Action-Based POM Pattern**: Merapikan Page Object dengan Action Method yang konsisten dan anti micro-functions.
- [x] **Reuse Authentication State**: Menyimpan status login (cookies) ke `.auth/state.json` via fixture `global_login` dan memuatnya ke `logged_in_page`, memangkas waktu eksekusi test secara masif.
- [x] **Network Interception & API Response**: Menggunakan `page.expect_response()` untuk memastikan API background sudah membalas request (pada Search, Reset, dan Login).
- [x] **Negative Test Case & Edge Cases**: Menguji validasi form kosong (`test_add_user_empty` & `test_login_empty_field`).
- [x] **Hybrid API Data Seeding & Teardown**: Setup data uji via REST API (`page.request.post`) dan otomatis dibersihkan via DELETE (`page.request.delete`), membuat test 100% mandiri (*self-contained*).
- [x] **HTML Reporting**: Mengonfigurasi `allure-pytest` dengan metadata `@allure.title` untuk menghasilkan laporan pengujian interaktif yang profesional.

---

## 💡 Poin Penting & Pelajaran

1. **Jangan hardcode selector** di test langsung — kumpulkan semua selector di `__init__()` Page Object.
2. **`filter(has_text=)`** sangat berguna untuk narrow down elemen yang punya class CSS sama tapi label berbeda.
3. **Data dinamis** (seperti username) harus di-generate via data factory dengan UUID agar tidak terjadi tabrakan data antar-run.
4. **`.wait_for(state="hidden")`** dan **`.wait_for(state="visible")`** penting untuk handle elemen async (seperti dropdown autocomplete OrangeHRM).
5. **Scope fixture `session`** untuk browser = efisiensi (tidak buka/tutup browser tiap test), tapi context & page tetap `function` scope agar test terisolasi.
6. **Auto-waiting sebelum membaca teks**: Pastikan elemen `to_be_visible()` terlebih dahulu sebelum memanggil `.inner_text()` untuk mencegah *race condition*.
