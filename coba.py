def enkripsi(teks, a, b):
  """
  Fungsi untuk mengenkripsi teks menggunakan Affine Cipher.

  Args:
    teks: Teks asli yang ingin dienkripsi.
    a: Nilai 'a' dalam rumus Affine Cipher.
    b: Nilai 'b' dalam rumus Affine Cipher.

  Returns:
    Teks terenkripsi.
  """
  teks = teks.upper()

  teks_enkripsi = ""

  for char in teks:

    angka_char = ord(char) - ord('A')

    angka_enkripsi = (a * angka_char + b) % 26

    char_enkripsi = chr(angka_enkripsi + ord('A'))

    teks_enkripsi += char_enkripsi

  return teks_enkripsi
