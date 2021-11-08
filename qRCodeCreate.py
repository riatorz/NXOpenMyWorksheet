import qrcode
img=qrcode.make('2108040;3;08092021;Aliminum;---;---')#DrawingCodeNumber-Drawing-Date-Mat-PartNumber-HeatTreatment(ExtraProcess)
img.save('2108040_02.png')
