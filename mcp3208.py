import LCD1602
import spidev, time
spi = spidev.SpiDev()

spi.open(0,0)
//
def analog_read(channel):

    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])

    adc_out = ((r[1]&15) << 8) + r[2]

    return adc_out


while True:
    LCD1602.init(0x27, 1)
    reading = analog_read(0) #อ่านค่าอนาล็อคขาที่ 0 แล้วเอาไปเก็บใน reading
    print reading
    result = (reading * 100) / 4095 #หาค่าเปอร์เซ็นของค่า reading แล้วเก็บไว้ใน result
    print result
    LCD1602.write(0,0, "Gas Level") #ปริ้นค่าออกทาง LCD1602
    LCD1602.write(1,1, "%f"%result) #แสดงค่าในรูปแบบทศนิยมสองต่ำแหน่ง
    time.sleep(1)
