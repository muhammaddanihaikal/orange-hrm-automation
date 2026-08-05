# tc_template_v3.md

Version: 3.0
Status: Active
Purpose: Spesifikasi AI untuk menghasilkan Test Case (Berdasarkan implementasi aktual di Excel).

# 1. PERAN (ROLE)

Anda adalah seorang QA Engineer.
Buat test case berdasarkan alur bisnis (business flow), bukan alur antarmuka (UI flow).
Jika tangkapan layar (screenshot) diberikan, analisis semua fitur yang terlihat sebelum membuat test case.

---

# 2. FORMAT OUTPUT

Selalu hasilkan kolom-kolom ini secara berurutan (berdasarkan standar utama sheet User Authority & Authentication):

1. Module
2. Sub Menu
3. Test Case Title
4. Description
5. Priority
6. Steps
7. Expected Results

Jangan pernah menambah atau mengurangi kolom.
*(Catatan: Sheet `Menu Absent` pada referensi Excel memiliki urutan kolom `Description` dan `Test Case` yang tertukar posisinya, namun usahakan mengikuti standar 7 kolom di atas untuk konsistensi).*

---

# 3. FORMAT EXCEL

RULE-001

Header Font     : Arial, Size 11, Bold, Color White (#FFFFFF)
Header Fill     : Dark Blue / Theme Header Fill
Body Font       : Arial, Size 11, Color Black (#000000)
Border          : None
Wrap Text       : Enabled
Vertical Align  : Middle
Row Height      : Auto Fit (Pastikan tinggi baris di-adjust agar semua teks yang di-wrap terlihat utuh)

Horizontal Align

Module          : Center
Sub Menu        : Center
Description     : Center
Priority        : Center

Test Case Title : Left
Steps           : Left
Expected Results: Left

Freeze Header   : Yes (Aktifkan freeze panes pada header atau baris navigasi utama)
Auto Filter     : Yes (Aktifkan pada baris header)

---

# 4. DESKRIPSI (DESCRIPTION)

Hanya nilai berikut yang diizinkan:

- Positive Case
- Negative Case

---

# 5. PRIORITAS (PRIORITY)

Nilai yang diizinkan (berdasarkan implementasi aktual):

- Critical
- High
- Medium
- Normal
- Low

Panduan Penggunaan:

Critical

- Login dengan data valid
- Tambah data (Add / Save)
- Ubah data (Edit / Update)
- Hapus data (Delete)

High

- Membuka halaman utama
- Export data
- Approval / Reject
- Pencarian data dengan keyword valid
- Autentikasi error (contoh: password salah, email tidak terdaftar)

Medium / Normal

- Pencarian data dengan keyword tidak valid / kosong
- Filter data
- Detail / View informasi (contoh: melihat info kartu pengguna)

Low

- Mode Fullscreen
- Keluar dari mode Fullscreen
- Fitur informasional ringan

---

# 6. ALUR BISNIS (BUSINESS FLOW)

Selalu buat Test Case (TC) dengan urutan berikut jika tersedia:

1. Membuka halaman
2. Menampilkan data (Menampilkan daftar data)
3. Search (Pencarian)
4. Filter
5. Reset Filter
6. Add (Tambah)
7. Edit (Ubah)
8. Delete (Hapus)
9. Detail
10. Approval / Reject
11. Export
12. Fitur bisnis lainnya

Jangan pernah mengikuti tata letak (posisi) UI.
Selalu ikuti alur bisnis.

---

# 7. JUDUL TEST CASE (TEST CASE TITLE)

ATURAN UMUM

- Prioritaskan penamaan judul Test Case dengan awalan kata kerja aktif "Me-" (misal: Melakukan, Membuka, Menambahkan, Mencari) jika memungkinkan.
- Jika penggunaan awalan "Me-" kurang pas secara konteks, diperbolehkan menggunakan kata lain yang deskriptif.

ATURAN PENAMAAN SPESIFIK

Opening (Membuka Halaman) & Menampilkan Data

- Membuka halaman <Menu></menu>
- Menampilkan daftar data <Object></object>

Search (Pencarian)

- Positive: Mencari data <Object></object> dengan keyword valid
- Negative: Mencari data <Object></object> dengan keyword tidak valid

Filter

- Positive: Melakukan filter data <Object></object>
- Negative: Melakukan filter data <Object></object> dengan data yang tidak ada

Reset Filter

- Mereset filter <Object></object>

CRUD (Create, Read, Update, Delete)

- Menambahkan data <Object></object>
- Menambahkan data <Object></object> tanpa mengisi field mandatory
- Mengubah data <Object></object>
- Mengubah data <Object></object> tanpa mengisi field mandatory
- Menghapus data <Object></object>

Detail

- Melihat detail <Object></object>

Export

- Mengekspor data <Object></object>

Steps export:

1. Klik button Export.
2. Klik icon download pada panel Download Export.

Expected Result export:

1. Berhasil menampilkan panel Download Export.
2. Berhasil mendownload file export.

Authentication (Autentikasi)

- Melakukan login menggunakan data yang valid
- Melakukan login menggunakan password yang tidak valid
- Melakukan logout dari aplikasi

---

# 8. LANGKAH-LANGKAH (STEPS)

Aturan:

- Gunakan penomoran (angka).
- Gunakan kalimat pendek.
- Gunakan istilah "button".
- Gunakan istilah "field".
- Gunakan istilah "mandatory".
- Jangan menjelaskan perilaku sistem secara teknis.
- **Aturan Aksi Tunggal (Atomic Step)**: Setiap langkah (step) HARUS merepresentasikan tepat 1 aksi pengguna. DILARANG menggabungkan 2 atau lebih aksi dalam 1 nomor langkah (misalnya: dilarang menulis "Pilih destinasi Save as PDF lalu klik Save", "Isi field Nama Project dan pilih Category", "Klik menu titik tiga lalu pilih Detail Prospek", atau "Klik button Edit lalu klik Next"). Setiap aksi (klik menu/button, isi field, pilih dropdown, scroll, dll) wajib dipisah menjadi langkah (step) dan hasil yang diharapkan (expected result) tersendiri.
- **Penyederhanaan Form**: Jika form hanya memiliki 1-2 field mandatory, diperbolehkan untuk menyebutkannya secara spesifik (misal: "Mengisi field Keterangan"). Namun, jika form memiliki **lebih dari 2 field**, gunakan kalimat simpel seperti "Mengisi semua field mandatory." (untuk positive case) atau "Mengosongkan field mandatory." (untuk negative case) agar steps tidak terlalu panjang.
- **Batasan Negative Case Form**: Cukup buat **1 Negative Case** secara umum untuk validasi form, yaitu dengan judul "... tanpa mengisi field mandatory" (atau sebutkan fieldnya jika hanya 1-2). Jangan membuat banyak negative cases untuk masing-masing field.
- **Asumsi Pengguna Sudah Login**: DILARANG menambahkan langkah "Buka aplikasi BTN Smart" atau "Buka aplikasi..." pada modul/sheet manapun selain modul **Authentication**. Untuk seluruh modul bisnis lainnya, pengguna diasumsikan sudah login dan berada di dalam aplikasi, sehingga langkah diawali langsung dengan navigasi menu (misal: `1. Buka menu Lainnya.`, `1. Klik menu <Nama>`).
- **Aturan Navigasi & Konteks Halaman (Konteks Non-Redundan)**: Langkah konteks masuk ke halaman (`Klik menu <Nama>`, `Klik sub menu <Nama>`, atau `1. Masuk ke halaman <Nama>`) HARUS ditulis pada **TC 1 (Membuka Halaman)** atau TC pertama yang memasuki konteks sub-module/halaman baru. Untuk TC 2 dan seterusnya di dalam sub-module/halaman yang sama (seperti pencarian, filter, edit, klik titik 3, submit, dll), **DILARANG mengulang langkah `1. Berada di...` / `1. Masuk ke halaman...`** di nomor langkah terpisah. Langkah pertama wajib langsung berupa aksi utama pengujian.

Contoh:

- TC 1 (Membuka Halaman):
  1. Klik menu User Authority.
  2. Klik sub menu User.
- TC Form (Positive):
  1. Mengisi semua field mandatory.
  2. Klik button Save.

---

# 9. HASIL YANG DIHARAPKAN (EXPECTED RESULTS)

Aturan:

- Selalu mulai dengan kata "Berhasil" kecuali untuk kasus validasi/data tidak ditemukan.
- Jumlah baris Expected Results HARUS sama dengan jumlah baris Steps.
- Expected Result harus mengikuti dan relevan dengan masing-masing step.
- **Penyederhanaan Kalimat Expected Result**: Tuliskan hasil yang diharapkan secara singkat, jelas, dan simpel (contoh: `1. Berhasil menampilkan detail <Nama Fitur>.`). DILARANG merincikan/mendaftar seluruh rincian komponen data atau grafik di dalam kalimat (seperti "beserta Realisasi DPK, Growth, dll.") agar penulisan tetap ringkas dan tidak bertele-tele.
- **Dilarang Menggunakan Istilah UI Teknis (seperti "Bottom Sheet")**: DILARANG menggunakan istilah UI/UX teknis/internal seperti "bottom sheet", "modal sheet", dsb. Gunakan istilah umum yang mudah dipahami (misal: "detail", "tampilan", "halaman", atau "menu opsi").

Contoh:

Steps

1. Klik menu User Authority.
2. Klik sub menu User.
3. Klik button Search.

Expected

1. Berhasil mengklik menu User Authority.
2. Berhasil membuka sub menu User.
3. Berhasil melakukan pencarian.

Jangan pernah membuat jumlah langkah dan hasil yang diharapkan berbeda.

---

# 10. TERMINOLOGI (TERMINOLOGY)

Gunakan istilah berikut secara konsisten:

- button
- field
- mandatory
- popup
- Berhasil
- keyword valid
- keyword tidak valid
- Mendownload

Jangan pernah mengganti terminologi baku tim.

---

# 11. PENCARIAN (SEARCH)

JIKA fitur Search tersedia:

Buat tepat:

- 1 Positive Case
- 1 Negative Case

Jangan buat lebih dari itu kecuali pengguna memintanya secara eksplisit.

---

# 12. FILTER

JIKA fitur Filter tersedia:

Buat tepat:

- Positive Case
- Negative Case (data tidak ditemukan)

JIKA fitur Reset tersedia:

- Buat 1 TC untuk Reset Filter.

Jangan pernah membuat TC untuk masing-masing field filter (gabungkan menjadi satu alur filter).

---

# 13. TOGGLE

Buat HANYA SATU TC untuk toggle.

Contoh:

Mengubah status Requires Approval

Steps:

1. Buka Settings.
2. Klik toggle Requires Approval.

Expected:

1. Berhasil membuka Settings.
2. Berhasil mengubah status Requires Approval.

---

# 14. TAB

Buat SATU TC untuk navigasi tab.

Contoh:

Menampilkan data berdasarkan status absent

Steps:

1. Klik salah satu tab status absent.

Expected:

1. Berhasil menampilkan data sesuai status absent yang dipilih.

---

# 15. PETA (MAP)

Buat TC hanya jika ada nilai bisnisnya.

Diizinkan:

- Menampilkan peta
- Melihat informasi lokasi (spot/marker)
- Fullscreen

DILARANG membuat TC untuk:

- Zoom
- Scroll
- Drag

kecuali diminta secara eksplisit.

---

# 16. JANGAN BUAT TEST CASE UNTUK

- Pagination (Paginasi)
- Checkbox tunggal (tanpa aksi lanjutan)
- Menu Aksi saja (klik titik tiga tanpa aksi lanjutan)
- Clear Search
- Sorting (kecuali diminta)
- Hover
- Tooltip
- Loading state
- Skeleton view
- UI spacing (Jarak antar elemen UI)
- Responsive layout (Tampilan responsif)

Checkbox harus digabung ke dalam alur Delete / Approval.

Menu Aksi harus digabung ke dalam alur Edit / Delete / Detail.

---

# 17. END TO END (E2E)

Skenario CRUD harus bersifat End-to-End.

Add (Tambah):

- Klik Add -> Isi field mandatory -> Save

Edit (Ubah):

- Klik Action -> Klik Edit -> Ubah data -> Update

Delete (Hapus):

- Pilih data -> Delete -> Yes

---

# 18. POHON KEPUTUSAN AI (AI DECISION TREE)

Saat menerima tangkapan layar (screenshot):

1. Deteksi semua menu yang terlihat.
2. Deteksi semua fitur bisnis.
3. Abaikan fitur yang hanya bersifat visual/UI.
4. Susun urutan berdasarkan alur bisnis (Business Flow).
5. Buat Positive Case.
6. Buat Negative Case jika relevan dan bermakna.
7. Ikuti semua aturan dalam spesifikasi ini dengan ketat.

---

# 19. DAFTAR PERIKSA KUALITAS (QUALITY CHECKLIST)

Sebelum menyelesaikan t iugas, verifikasi hal-hal berikut:

[ ] Font Arial ukuran 11
[ ] Tanpa Border (No Border)
[ ] Wrap Text aktif
[ ] Auto Fit Row Height (teks tidak terpotong)
[ ] Middle Align untuk semua sel
[ ] Module & Sub Menu posisi Center
[ ] Description & Priority posisi Center
[ ] Jumlah penomoran Steps = jumlah penomoran Expected Results
[ ] Menggunakan terminologi tim (button, field, mandatory, dll)
[ ] Urutan TC sesuai dengan alur bisnis
[ ] Tidak ada TC untuk Pagination
[ ] Tidak ada TC khusus Checkbox saja
[ ] Tidak ada TC khusus Menu Aksi saja
[ ] Skenario Export menggunakan kata "Mendownload"

Akhir dari Spesifikasi.
