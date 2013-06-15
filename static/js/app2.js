
App = Ember.Application.create({});

App.ApplicationController = Ember.Controller.extend({
    message: 'This is the application template' 
});

 App.Router.map(function() {
    this.route("index", { path: "/" });
    this.route("list", { path: "/list" });
  });
  
  App.IndexController = Ember.Controller.extend({
    message: 'Hello! See how index.hbs is evaluated in the context of IndexController' 
  });

  App.ListRoute = Ember.Route.extend({
    setupController: function(controller) {
      controller.set('content', ['angular.js', 'backbone.js', 'ember.js']);
    }
  });

