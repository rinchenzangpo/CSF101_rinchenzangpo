import phonenumbers
from phonenumbers import geocoder
import time, random

def start_phone_tracer(target):
    print(f"[+] PhoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace...")
    
    try:
        # Parse the number (assuming it's in international format if no region given)
        p = phonenumbers.parse(target, "None")  # Change "US" to default region if needed
        r = geocoder.description_for_number(p, "en")
        
        print(f"[+] Location: {r if r else 'Unknown'}")
    except Exception as e:
        print(f"[!] Error: {e}")
    
    print(f"[+] Trace Complete")

# Example usage
start_phone_tracer("+975-17262795")
