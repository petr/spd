var _ = require('_');
var Backbone = require('backbone');
var ImageTaskModel = require('models');
/*
https://learn.javascript.ru/xhr-onprogress
https://github.com/azproduction/lmd/wiki/Modules-naming-expressions
*/

var UploadView = Backbone.View.extend({
    el: '.js-main-container',
    template: _.template(require('templates/upload')),
    events: {
        'submit': 'upload',
    },
    upload: function(event) {
        event.preventDefault();
        var file = this.$('#js-image-file')[0].files[0];
        this.model.upload(file);
    }
});

var ProcessingView = Backbone.View.extend({
    template: _.template(require('templates/processing'))
});

var ErrorView = Backbone.View.extend({
    template: _.template(require('templates/error'))
});

var SuccessView = Backbone.View.extend({
    template: _.template(require('templates/success'))
});

var MainView = Backbone.View.extend({
    el: '.js-main-container',
    events: {
        'click .js-try-again': 'reset'
    },
    views: {
        'upload': UploadView,
        'processing': ProcessingView,
        'error': ErrorView,
        'success': SuccessView
    },
    initialize: function(options) {
        this.createTaskModel();
    },
    render: function(name, attributes) {
        var name = name ? name: 'upload';
        if (this.currentView) {
            this.currentView.undelegateEvents();
        }
        this.currentView = new this.views[name]({'model': this.model});
        this.$el.html(this.currentView.template(attributes));
        return this;
    },
    error: function(model, response) {
        var error = response.responseJSON['image'][0];
        this.render('error', {'error': error});
    },
    processing: function() {
        this.render('processing');
    },
    success: function() {
        this.render('success');
    },
    reset: function(event) {
        event.preventDefault();
        this.stopListening(this.model);
        this.model = new ImageTaskModel();
        this.createTaskModel();
        this.render();
    },
    createTaskModel: function() {
        this.model = new ImageTaskModel();
        this.listenTo(this.model, 'error', this.error);
        this.listenTo(this.model, 'processing', this.processing);
        this.listenTo(this.model, 'success', this.success);
    }
});

module.exports = MainView;