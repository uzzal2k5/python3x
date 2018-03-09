import pyotp
import time
import numbers
from random import randint

 # Time Based OTP
totp = pyotp.TOTP("base32secret3232")
otp = totp.now()
otp_v = totp.verify(otp)
print("Current OTP : ", otp)
print(otp_v)
# otp_rev = totp.verify(otp, time.sleep(30))
# print(otp_rev)

# Counter Based OTP's'
# Generate Random Counter using random

hotp = pyotp.HOTP('base32secret3232')
c = randint(0, 9)
couter_otp = hotp.at(c)
couter_otp2 = hotp.generate_otp(c)
print('Counter OTP : %s  %s', couter_otp,c)
print('2nd Current OTP : ', couter_otp2, c)

otp_c_v = hotp.verify(couter_otp2, c)
print(c)
print(otp_c_v)
c = c + 1
otp_c_rev = hotp.verify(couter_otp, c + 1)
print(c)
print(otp_c_rev)


# # Generate a base32 Secret Key
#  returns a 16 character base32 secret. Compatible with Google
# ˓→Authenticator and other OTP apps
sec_otp = pyotp.random_base32()
print(sec_otp)


# Google Authenticator Compatible
# function


# def getGoogleOtp():
#     pass


class GetOtp():
    def getSecOtp(otp_string, option):
            google_otp = pyotp.TOTP(otp_string);
            google_sec_otp = google_otp.provisioning_uri(option);
            return google_sec_otp

    def getCounterOtp(otp_string, option):
            google_otp = pyotp.HOTP(otp_string)
            count = randint(0, 9)
            google_otp_generate = google_otp.generate_otp(count)
            print('Counter OTP : ', google_otp_generate, count)
            google_counter_otp = google_otp.provisioning_uri(option,count)
            veri = google_otp.verify(google_otp_generate,count)
            print('verification : ', veri)
            return google_counter_otp

    def optVerify(self, otp, c ):
            otp_verify = GetOtp.getCounterOtp().verify(otp,c)
            return otp_verify


# print('Counter Number: ', c)
option = "'uzzal2k5@gmail.com',issuer_name='Secret Apps'"


otp = GetOtp.getCounterOtp(sec_otp, option)
print("This is the counter based OTP\n ")
print(otp)


# print(GetOtp.optVerify(otp,c))
# sec_otp = pyotp.random_base32()
# hotp = pyotp.HOTP(sec_otp)
# veri = hotp.verify(otp,c - 1)
# print("Verify OTP : ", veri)

# print(google_otp)
# print(google_sec_otp)


