
# Your configuration should follow the following format :
# Replace the __XXX__ with the inteded value

#meta = dict(
#	__METANAME1__ = 
#		dict( __NODESET1__ = 
#			dict ( services = [ "__SERVICE1__" , "__SERVICE2__" )
#		)
#)

meta = dict(
	web =
		dict( 
			test1 =	dict ( services = ["apache2"] ),
			test2 = dict ( services = ["ntp","mysql"] )
		),
	clock =
		dict(
			test1 = dict( services = ["ntp"] ),
			test2 = dict( services = ["ntp"] )
		)
)
