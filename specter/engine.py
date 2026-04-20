import subprocess
import re

class SpecterEngine:
    def __init__(self):
        # Nmap tidak menggunakan API Key, jadi biarkan kosong
        pass

    def search_radar(self, target_ip, stealth_mode=False):
        scan_type = "-sS" if stealth_mode else "-sT"
        
        command = ["nmap", scan_type, "-p", "554", "--open", target_ip]
        
        try:
            # Menjalankan Nmap langsung di terminal latar belakang
            process = subprocess.run(command, capture_output=True, text=True)
            output = process.stdout
            
            matches = []
            current_ip = None
            
            # Membedah teks hasil Nmap
            for line in output.split('\n'):
                # Mencari baris yang mengandung IP Address
                ip_match = re.search(r"Nmap scan report for ([\d\.]+)", line)
                if ip_match:
                    current_ip = ip_match.group(1)
                
                # Jika menemukan port terbuka, simpan ke daftar target
                if "554/tcp" in line and "open" in line and current_ip:
                    matches.append({
                        'ip_str': current_ip,
                        'port': 554,
                        'org': 'Local/Direct Target' # Nmap tidak tahu nama Organisasi
                    })
                    
            return matches

        except Exception as e:
            return f"Nmap Execution Failed: {str(e)}"