<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Caesar Cipher Tool</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px auto;
      max-width: 600px;
      background-color: #f8f9fa;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    textarea, input, button {
      width: 100%;
      margin-bottom: 10px;
      padding: 10px;
      font-size: 1em;
      border-radius: 5px;
      border: 1px solid #ccc;
    }

    button {
      background-color: #007bff;
      color: white;
      cursor: pointer;
      transition: background-color 0.2s ease;
    }

    button:hover {
      background-color: #0056b3;
    }

    .output {
      margin-top: 20px;
    }

    .output p {
      background-color: #e9ecef;
      padding: 10px;
      border-radius: 5px;
    }

    .error {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <h1>Caesar Cipher Encrypt/Decrypt</h1>

  <label for="message">Enter your message:</label>
  <textarea id="message" rows="4" placeholder="Type your message here..."></textarea>

  <label for="shift">Enter the shift value:</label>
  <input type="number" id="shift" placeholder="e.g., 3">

  <button onclick="runCipher()">Encrypt & Decrypt</button>

  <div class="error" id="errorMsg"></div>

  <div class="output">
    <h3>Encrypted Message:</h3>
    <p id="encrypted">—</p>

    <h3>Decrypted Message:</h3>
    <p id="decrypted">—</p>
  </div>

  <script>
    function caesarEncrypt(text, shift) {
      let result = '';
      for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char.match(/[a-z]/i)) {
          let code = text.charCodeAt(i);
          let base = (code >= 65 && code <= 90) ? 65 : 97;
          result += String.fromCharCode((code - base + shift + 26) % 26 + base);
        } else {
          result += char;
        }
      }
      return result;
    }

    function runCipher() {
      const text = document.getElementById('message').value;
      const shiftInput = document.getElementById('shift').value;
      const errorMsg = document.getElementById('errorMsg');
      const encryptedOutput = document.getElementById('encrypted');
      const decryptedOutput = document.getElementById('decrypted');

      errorMsg.textContent = '';
      encryptedOutput.textContent = '—';
      decryptedOutput.textContent = '—';

      const shift = parseInt(shiftInput);

      if (!text.trim()) {
        errorMsg.textContent = 'Please enter a message.';
        return;
      }

      if (isNaN(shift)) {
        errorMsg.textContent = 'Please enter a valid numeric shift value.';
        return;
      }

      const encrypted = caesarEncrypt(text, shift);
      const decrypted = caesarEncrypt(encrypted, -shift);

      encryptedOutput.textContent = encrypted;
      decryptedOutput.textContent = decrypted;
    }
  </script>

</body>
</html>

