from app import db, Dokumen, app

# Memasukkan data ke dalam database
with app.app_context():
    doc1 = Dokumen(judul="Plagiarism Check", konten="Ini adalah isi Plagiarism Check.")
    db.session.add(doc1)
    db.session.commit()
    print("Selamat! Data Anda sudah berhasil masuk ke database.")

# Mengecek apakah data sudah ada
with app.app_context():
    semua_dokumen = Dokumen.query.all()
    print(f"Jumlah dokumen di database: {len(semua_dokumen)}")
    for doc in semua_dokumen:
        print(f"- {doc.judul}")