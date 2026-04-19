import subprocess
import re

class SpecterEngine:
    def init(self, api_key=None):
        # API Key sekarang tidak diperlukan untuk mode mandiri (Ghost Engine)
        pass

    def search_radar(self, target_range, stealth_mode=True):
        """
        target_range: Bisa berupa IP (192.168.1.1) atau CIDR (110.10.0.0/16)
        stealth_mode: Jika True, gunakan template -T2 (lambat tapi aman)
        """
        # Command Nmap:
        # -sS: Stealth SYN Scan (tidak menyelesaikan jabat tangan TCP)
        # -p 554: Port target (CCTV/RTSP)
        # -T2 atau -T3: Kecepatan diatur agar menyeimbangkan stealth dan efisiensi
        # --randomize-hosts: Agar urutan IP yang discan tidak urut (mengecoh IDS)
        
        timing = "-T2" if stealth_mode else "-T3"
        
        cmd = [
            "nmap", "-sS", "-p", "554", 
            timing, 
            "--randomize-hosts", 
            "--open", 
            target_range
        ]

        try:
            # Menjalankan scan. stderr dialihkan ke DEVNULL agar pesan peringatan tidak bocor ke terminal
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            stdout, _ = process.communicate()
            
            # Parsing hasil output Nmap untuk mendapatkan IP target
            matches = []
            found_ips = re.findall(r'Nmap scan report for (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', stdout)
            
            for ip in found_ips:
                matches.append({
                    'ip_str': ip,
                    'org': 'Infiltrated Host',
                    'port': 554
                })
                
            return matches
        except Exception as e:
            return f"Scanning Error: {str(e)}"
