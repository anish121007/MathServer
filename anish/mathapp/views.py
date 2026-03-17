from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
def Calculate_bill(request):
	price=float(request.POST.get('price','0'))
	gst=float(request.POST.get('GST','0'))
	total = price+(price*gst/100) if request.method=='POST' else 0
	print("Price=",price)
	print("GST=",gst)
	print("Total=",total)
	return render(request,"mathapp/math.html",{'Price':price,'GST':gst,'Total':total})