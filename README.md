# مشروع: أداة تشفير وفك تشفير الملفات (File Encryption/Decryption Tool)

## الوصف (Arabic Description for Scholarship Application)

**اسم المشروع:** أداة تشفير وفك تشفير الملفات باستخدام خوارزمية Fernet المتماثلة.

**الهدف:** تطوير أداة سطر أوامر بسيطة لكنها قوية تسمح للمستخدمين بتأمين ملفاتهم الحساسة عن طريق تشفيرها وفك تشفيرها باستخدام مفتاح سري واحد. يهدف المشروع إلى تطبيق المفاهيم الأساسية للتشفير المتماثل (Symmetric Cryptography)، وهو حجر الزاوية في أمن المعلومات.

**التقنيات المستخدمة:**
*   **لغة البرمجة:** Python
*   **المكتبة:** `cryptography` (Fernet implementation)
*   **المفهوم الأمني:** التشفير المتماثل (Symmetric Encryption)

**الإنجازات:**
*   إنشاء مفتاح تشفير عشوائي وقوي لمرة واحدة (One-time Key Generation).
*   تطبيق وظائف التشفير وفك التشفير للملفات الثنائية (Binary Files)، مما يضمن حماية البيانات من الوصول غير المصرح به.
*   إظهار فهم عملي لكيفية استخدام مكتبات التشفير الموثوقة لتأمين البيانات.

---

## Project: File Encryption/Decryption Tool

**Project Name:** File Encryption/Decryption Tool using Symmetric Fernet Algorithm.

**Goal:** To develop a simple yet robust command-line utility that allows users to secure their sensitive files by encrypting and decrypting them using a single secret key. The project aims to practically apply the core concepts of Symmetric Cryptography, a cornerstone of Information Security.

**Technologies Used:**
*   **Programming Language:** Python
*   **Library:** `cryptography` (Fernet implementation)
*   **Security Concept:** Symmetric Encryption

**Key Features:**
*   Secure, one-time key generation.
*   Encryption and decryption functions for any binary file.
*   Demonstrates a practical understanding of using reliable cryptographic libraries for data protection.

## How to Run (Technical Instructions)

1.  **Installation:**
    ```bash
    pip3 install cryptography
    ```
2.  **Generate Key:**
    ```bash
    python3 encryptor.py generate
    # This creates a file named 'secret.key'
    ```
3.  **Encrypt a File:**
    ```bash
    # Create a test file first
    echo "This is a secret message." > test_file.txt
    python3 encryptor.py encrypt test_file.txt
    # A new file 'test_file.txt.enc' will be created, and 'test_file.txt' will be deleted.
    ```
4.  **Decrypt a File:**
    ```bash
    python3 encryptor.py decrypt test_file.txt.enc
    # The file 'test_file.txt.enc' will be decrypted back to 'test_file.txt'.
    ```
