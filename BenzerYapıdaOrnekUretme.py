import random

def uretilen_samples(base_line, num_samples):
    # Sabit olan ilk 5 karakteri ayır
    prefix = base_line[:5]

    # Boş bir liste oluştur
    uretilen_samples = []

    for _ in range(num_samples):
        # Kalan karakterleri rastgele değiştirerek yeni bir satır oluştur, Oluşturulan satırı listeye ekle
        random_chars = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(len(base_line) - 5)]
        new_line = f"{prefix}{''.join(random_chars)}"        
        uretilen_samples.append(new_line)

    return uretilen_samples

def write_to_file(samples, file_path):
    # Örnekleri dosyaya yaz
    with open(file_path, 'w') as file:
        for sample in samples:
            file.write(f"{sample}\n")

# Verilen örnekten başlayarak 100,000 örnek üret
base_line = "NH9CK7J7P3"
num_samples = 100000
uretilen_samples = uretilen_samples(base_line, num_samples)
print(uretilen_samples)

# Örnekleri bir text dosyasına yaz
file_path = "uretilen_samples.txt"
write_to_file(uretilen_samples, file_path)

print(f"{num_samples} ornek uretildi ve text dosyasına kayıt edildi {file_path}")
