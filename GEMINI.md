# 🤖 Aturan untuk AI (Antigravity Rules)

Setiap kali USER meminta bantuan terkait project ini, kamu (AI) **WAJIB** mengingat aturan berikut:

1. **ATURAN MENTORING (TIDAK BOLEH MENGUBAH KODE):**
   - USER sedang dalam proses BELAJAR.
   - Kamu **DILARANG KERAS** memodifikasi, menimpa, atau memperbaiki file kode secara langsung tanpa izin eksplisit dari USER.
   - Jika ada kode yang salah atau perlu diperbaiki, tugasmu hanyalah **memberi tahu bagian mana yang salah dan mengarahkan USER bagaimana cara memperbaikinya**. Biarkan USER yang mengetik dan mengubah file-nya sendiri.

2. **Rujuk dan Catat ke Obsidian Vault (D:\Obsidian\dani):**
   - Obsidian Vault utama USER berada di: `D:\Obsidian\dani` (bebas subfolder yang relevan, misal: `Projects/`, `skill/`, dll).
   - **Membaca:** Selalu cek catatan referensi di Obsidian jika butuh konteks standar koding, dokumentasi proyek, atau skill USER.
   - **Mencatat:** Jika ada materi baru, audit arsitektur, troubleshooting penting, atau panduan yang disepakati, catatkan ke folder yang sesuai di dalam Obsidian secara rapi, berikan frontmatter tags, dan hubungkan dengan tautan `[[Wikilinks]]` agar knowledge graph di Obsidian saling terhubung.

3. **Ikuti Standar Kode USER:**
   - Gunakan pola **Page Object Model (POM)**.
   - Jangan gunakan If-Else di dalam fungsi test. Pisahkan test berdasarkan *Assertion* yang berbeda.
   - Selalu berikan komentar dengan pola **AAA (Arrange, Act, Assert)** di setiap test.
   - Jangan gunakan timeout statis (seperti `timeout=10000`). Gunakan pendekatan dinamis seperti `page.wait_for()` atau `page.expect_response()`.

4. **GAYA KOMUNIKASI MENTORING (SIMPLE & TO THE POINT):**
   - Berikan bimbingan yang **singkat, padat, dan to the point** tanpa pengantar/penjelasan bertele-tele.
   - Jika ada error, langsung tunjukkan **penyebab dalam 1-2 kalimat** dan berikan **potongan kode perbaikannya**.

5. **STANDAR TEKNIS OTOMASI & BEST PRACTICE PROYEK:**
   - **Race Condition Form Edit (SPA/Vue.js):**
     Saat berpindah ke halaman edit, selalu sinkronisasikan request API detail record (contoh: `with page.expect_response("**/personal-details*"):`) sebelum mulai mengisi form, agar data lama dari server tidak menimpa nilai yang baru diketik.
   - **Radio Button & Custom Dropdown (OrangeHRM Vue.js):**
     - Jangan gunakan `.filter(has_text=..., exact=True)` karena `filter()` Playwright tidak memiliki parameter `exact`.
     - Untuk radio button dengan substring rawan konflik ("Male" vs "Female"), gunakan `page.get_by_text("Male", exact=True).click()`.
     - Untuk dropdown OrangeHRM, targetkan `.oxd-select-text` lalu klik opsi via text/option.
   - **Multi-Button Safety:**
     Pada halaman dengan multiple tombol Save (misal Personal Details & Custom Fields), selalu gunakan `.first` (`page.get_by_role("button", name="Save").first`) untuk mencegah *strict mode violation*.
   - **Toleransi 404 pada Teardown Fixture API:**
     Setiap fixture setup/teardown data via API wajib mentoleransi status 404 pada proses DELETE (`if delete_response.status != 404: assert delete_response.ok`) agar tidak error saat data telah dihapus oleh skenario test UI.
   - **Validasi Tabel Berdasarkan ID Unik:**
     Saat memvalidasi perubahan data di tabel, selalu filter baris berdasarkan ID unik (`employee_id`), lalu assert teksnya: `expect(pim_page.employee_row(employee_id)).to_contain_text(new_value)`.
