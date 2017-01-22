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
    ## Gas Sensor ตัวที่หนึ่ง
    reading0 = analog_read(0) #อ่านค่าอนาล็อคขาที่ 0 แล้วเอาไปเก็บใน reading
    print reading0
    result0 = (reading0 * 100) / 4095 #หาค่าเปอร์เซ็นของค่า reading แล้วเก็บไว้ใน result
    print result0
    ## Gas Sensor ตัวที่สอง
    reading1 = anolog_read(1)
    print reading1
    result1 = (reading0 * 100) / 4095
    print result1
    ###ปริ้นค่าออกทาง LCD1602
    LCD1602.write(0,0, "%f"%result0) #แสดงค่าในรูปแบบทศนิยมสองต่ำแหน่ง
    LCD1602.write(1,1, "%f"%result1) #แสดงค่าในรูปแบบทศนิยมสองต่ำแหน่ง
    time.sleep(1)
