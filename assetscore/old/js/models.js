
var Backbone = require('Backbone');
var _ = require('_');

var TIMEOUT_BETWEEN_ATTEMPTS = 2 * 1000;


var ImageTaskModel = Backbone.Model.extend({
    urlRoot: '/api/tasks/',
    initialize: function(options) {
        this.listenTo(this, 'sync', this.poll);
        this.listenTo(this, 'change:status', this.changeStatus);
    },
    poll: function() {
        if (this.get('status') === 'processing') {
            _.delay(
                _.bind(
                    this.fetch,
                    this
                ),
                TIMEOUT_BETWEEN_ATTEMPTS
            );
        }
    },
    changeStatus: function() {
        if (this.get('status') === 'success') {
            this.trigger('success');
        }
    },
    upload: function(file) {
        if (this.isNew) {
            var formData = new FormData();
            formData.append('image', file);
            var options = {
                data: formData,
                processData: false,
                contentType: false
            };
            this.save({}, options);
            this.trigger('processing');
        } else {
            console.error('Trying to upload file to already exist model.');
        }
    }
});


module.exports = ImageTaskModel;
