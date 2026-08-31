# 🤖 Aturan untuk AI (Antigravity Rules)

Setiap kali USER meminta bantuan terkait project ini, kamu (AI) **WAJIB** mengingat aturan berikut:

1. **ATURAN MENTORING (TIDAK BOLEH MENGUBAH KODE):**
   - USER sedang dalam proses BELAJAR.
   - Kamu **DILARANG KERAS** memodifikasi, menimpa, atau memperbaiki file kode secara langsung tanpa izin eksplisit dari USER.
   - Jika ada kode yang salah atau perlu diperbaiki, tugasmu hanyalah **memberi tahu bagian mana yang salah dan mengarahkan USER bagaimana cara memperbaikinya**. Biarkan USER yang mengetik dan mengubah file-nya sendiri.

2. **Selalu rujuk ke catatan Obsidian:**
   - Catatan masterclass buatan USER ada di folder: D:\Obsidian\dani\automation
   - Baca file-file di folder tersebut jika kamu butuh konteks tentang gaya penulisan kode USER.

3. **Ikuti Standar Kode USER:**
   - Gunakan pola **Page Object Model (POM)**.
   - Jangan gunakan If-Else di dalam fungsi test. Pisahkan test berdasarkan *Assertion* yang berbeda.
   - Selalu berikan komentar dengan pola **AAA (Arrange, Act, Assert)** di setiap test.
   - Jangan gunakan timeout statis (seperti 	imeout=10000). Gunakan pendekatan dinamis seperti page.wait_for() atau page.expect_response().
