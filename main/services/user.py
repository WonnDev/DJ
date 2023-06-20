class UserService extends BaseService:
	contructor() 
		this.userMode = new UserModel;

	def getFood(data):
		food = Food.objects.all()
		serializer = this.userMode()
		return data

	def getFoods(data):	
		food = Food.objects.all()	
		serializer = this.userMode()
		return data