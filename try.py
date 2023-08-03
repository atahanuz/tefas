import http.client
import ssl

context = ssl.SSLContext()
context.options &= ~ssl.OP_NO_SSLv3 & ~ssl.OP_NO_TLSv1 & ~ssl.OP_NO_TLSv1_1
context.options |= ssl.OP_NO_RENEGOTIATION

conn = http.client.HTTPSConnection("www.tefas.gov.tr", context=context)
conn.request("GET", "/FonAnaliz.aspx?FonKod=AFT")
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))