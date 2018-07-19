import FreeCAD
import Part
#This takes the dimensions from the user.
def table(base_length, base_width, base_height,leg_thickness, leg_height):
#These are the placements of the table.
	make_cube(base_length, base_width, base_height, FreeCAD.Placement(FreeCAD.Vector(0,0,-leg_height),.Rotation(FreeCAD.Vector(0,0,1),0)))
	make_cube(leg_thickness,leg_thickness,leg_height, FreeCAD.Placement(FreeCAD.Vector(0,0,- (leg_height + leg_height )),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0)))
	make_cube(leg_thickness,leg_thickness,leg_height, FreeCAD.Placement(FreeCAD.Vector(base_length - leg_thickness,0,-(leg_height + leg_height)),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0)))
	make_cube(leg_thickness,leg_thickness,leg_height,FreeCAD.Placement(FreeCAD.Vector(0,base_width - leg_thickness,-(leg_height + leg_height)),FreeCAD.Rotation(V.Vector(0,0,1),0)))
	make_cube(leg_thickness,leg_thickness,leg_height, FreeCAD.Placement(FreeCAD.Vector(base_length - leg_thickness,base_width - leg_thickness,-(leg_height + leg_height)),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0)))
	FreeCAD.ActiveDocument.recompute()
	##Gui.SendMsgToActiveView("ViewFit")

#This function calls the above function five times.
def make_cube(length, width, height, placement):	
	cube_leg = FreeCAD.ActiveDocument.addObject("Part::Box","Box")
	FreeCAD.ActiveDocument.ActiveObject.Label = "legs"
	cube_leg.Length = length
	cube_leg.Width = width
	cube_leg.Height = height
	cube_leg.Placement = placement
	FreeCAD.ActiveDocument.recompute()
	
