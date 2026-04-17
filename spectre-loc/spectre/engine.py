import subprocess
import re

class SpectreEngine:
    def __init__(self, api_key=None):
        # API Key sekarang opsional/tidak diperlukan untuk mode mandiri
        pass

    def search_radar(self, target_range, stealth_mode=True):
        """
        target_range: Bisa berupa IP (192.168.1.1) atau CIDR (110.10.0.0/16)
        stealth_mode: Jika True, gunakan template -T1 (sangat lambat tapi aman)
        """
        # Command Nmap:
        # -sS: Stealth SYN Scan (tidak menyelesaikan jabat tangan TCP)
        # -p 554: Port target (CCTV/RTSP)
        # -T1 atau -T2: Kecepatan lambat agar tidak terdeteksi
        # --randomize-hosts: Agar urutan IP yang discan tidak urut (mengecoh IDS)
        
        timing = "-T1" if stealth_mode else "-T3"
        
        cmd = [
            "nmap", "-sS", "-p", "554", 
            timing, 
            "--randomize-hosts", 
            "--open", 
            target_range
        ]

        try:
            # Menjalankan scan dan menangkap outputnya
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            
            # Parsing hasil output Nmap untuk mendapatkan IP target
            matches = []
            # Mencari pola IP address dalam output nmap
            found_ips = re.findall(r'Nmap scan report for (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', stdout)
            
            for ip in found_ips:
                matches.append({
                    'ip_str': ip,
                    'org': 'Local Scan Result',
                    'port': 554
                })
                
            return matches
        except Exception as e:
            return f"Scanning Error: {str(e)}"
