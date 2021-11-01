from PIL import Image, ImageFont, ImageDraw

achergrond = Image.open("meme_background.jpg")
lettertype = ImageFont.truetype("impact.ttf", 40)



# De breedte en hoogte van de afbeelding lezen en tonen 


breedte = achergrond.width
hoogte = achergrond.height

tekengebied = ImageDraw.Draw(achergrond)

tekst = "Wanneer Ian 1 dag ziek is\nEn alle cosplay mist"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 1

tekst = "Wanneer Ian 1 dag ziek is\nEn alle cosplay mist"
tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

achergrond.show()

achergrond.save("meme_met_tekst.jpg")