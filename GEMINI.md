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
