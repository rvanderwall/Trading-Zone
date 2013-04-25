App = Ember.Application.create({
  users: [],
  selectedUser: null
});

  
App.Router.map(function() {
	this.resource('about'),
	this.resource('posts')
});

User = Ember.Object.extend({
    name: null,
	tasks: []
});

bob = User.create({name: "Bob"});
mark = User.create({name: "Mark"});

App.usersController.set("users",[bob,mark]);
