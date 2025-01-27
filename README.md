# Projekt2.0

W projekcie został zastosowany algorytm AES do szyfrowania i deszyfrowania wiadomości tekstowych.
Zaprezentowane zostało wstrzykiwanie SQL do kodu i sposób obrony przed tym atakiem za pomocą walidacji danych wejściowych.

Na potrzeby szyfrowania wiadomości została zainstalowana biblioteka cryptography w Pythonie

Funkcje:
Przykład szyfrowania i deszyfrowania dostępny pod endpointami /encrypt i /decrypt.
Endpoint /vulnerable-login pokazuje przykład podatności na SQL Injection.
Endpoint /secure-login przedstawia zabezpieczenie przy użyciu parametrów zapytań.
Automatyczne tworzenie bazy danych users.db przy pierwszym uruchomieniu.

Komendy w bash:
Do kodowania wiadomości 
curl -X POST http://127.0.0.1:5000/encrypt -H "Content-Type: application/json" -d '{"message": "Praca zaliceniowa"}'
 
![image](https://github.com/user-attachments/assets/ecf96a3c-07d5-48d3-bff0-6a569008a70f)

Do dekodowania wiadomości:
curl -X POST http://127.0.0.1:5000/decrypt -H "Content-Type: application/json" -d '{"encrypted_message": "(tekst który był zakodowany)" }'

 ![image](https://github.com/user-attachments/assets/b47f4014-7772-48b5-936b-f371df8cd602)


Do ataku SQL Injection:
curl -X POST http://127.0.0.1:5000/vulnerable-login -H "Content-Type: application/json" -d '{"username": "'\'' OR 1=1 --", "password": ""}'
 
![image](https://github.com/user-attachments/assets/19fb8a70-95cf-4b3a-af8a-4eb0e2ae8f77)

Do zalogowanie się bez możliwości wstrzykiwania SQL:
curl -X POST http://localhost:5000/secure-login   -H "Content-Type: application/json"   -d '{"username": "admin", "password": "12345"}'

 ![image](https://github.com/user-attachments/assets/e2b4a0d9-d000-44e3-b9b4-41704b0a8263)

można również sprawdzić czy można zalogować się metodą SQL Injection następującą komendą:
curl -X POST http://127.0.0.1:5000/secure-login -H "Content-Type: application/json" -d '{"username": "'\'' OR 1=1 --", "password": ""}'

![image](https://github.com/user-attachments/assets/30da6575-5b5a-4124-95c3-9818678d7a9b)

