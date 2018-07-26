import FreeCAD as App
import Part

def drum(radius_1, radius_2,height_1, height_2, height_3):
	circle1 = make_circle(radius_1, App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0)))
	circle2 = make_circle(radius_2, App.Placement(App.Vector(0,0,-height_1),App.Rotation(App.Vector(0,0,1),0)))
	circle3 = make_circle(radius_2, App.Placement(App.Vector(0,0,-(height_1+height_2)),App.Rotation(App.Vector(0,0,1),0)))
	circle4 = make_circle(radius_1, App.Placement(App.Vector(0,0,-(height_1+height_2+height_3)),App.Rotation(App.Vector(0,0,1),0)))
	circle5 = make_circle(radius_1, App.Placement(App.Vector(0,0,-(height_1+height_2+height_3)),App.Rotation(App.Vector(0,0,1),0)))
	
	

	loft = App.ActiveDocument.addObject('Part::Loft','Loft')
	loft.Sections  = [circle1, circle2]
	loft.Solid = False
	loft.Ruled = True
	App.ActiveDocument.recompute()



	loft1 = App.ActiveDocument.addObject('Part::Loft','Loft')
	loft1.Sections=[circle2, circle3]
	loft1.Solid = False
	loft.Ruled = True
	App.ActiveDocument.recompute()




	loft2 = App.ActiveDocument.addObject('Part::Loft','Loft')
	loft2.Sections=[circle3, circle4]
	loft2.Solid = False
	loft.Ruled = True
	App.ActiveDocument.recompute()




	f = App.ActiveDocument.addObject('Part::Extrusion', 'Extrude')
	f.Base = circle5
	f.DirMode = "Normal"
	f.LengthFwd = 10
	f.Solid = True
	App.ActiveDocument.recompute()


	compound = App.activeDocument().addObject("Part::Compound","Compound")
	compound.Links = [loft, loft1, loft2, f]
	App.ActiveDocument.recompute()

	compound.ViewObject.ShapeColor = (0.96,0.32,0.00)
	App.ActiveDocument.recompute()

	volume = ((3.14 * (radius_1 ** 2+ radius_1 * radius_2+ radius_2**2) * height_1)/3 + 3.14 * (radius_2 ** 2) * height_2 + (3.14 * (radius_1 ** 2 + radius_1 * radius_2+ radius_2**2) * height_3)/3)/1000000

	print "The volume of the drum is",volume,"L" 

def make_circle(radius,placement):
	circle = App.ActiveDocument.addObject("Part::Circle","Circle")
 	App.ActiveDocument.Circle.Label = "circle"
 	circle.Radius = radius
 	circle.Placement = placement
 	App.ActiveDocument.recompute()
	return circle




