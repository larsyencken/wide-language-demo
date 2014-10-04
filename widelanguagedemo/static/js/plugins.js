// place any jQuery/helper plugins in here, instead of separate, slower script files.

var languages = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  limit: 10,
  prefetch: {
    // url points to a json file that contains an array of country names, see
    // https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
    url: '/static/data/languages.json',
  }
});

// kicks off the loading/processing of `local` and `prefetch`
languages.initialize();

// passing in `null` for the `options` arguments will result in the default
// options being used
$('#prefetch .typeahead').typeahead(null, {
  name: 'languages',
  displayKey: 'code',
  // `ttAdapter` wraps the suggestion engine in an adapter that
  // is compatible with the typeahead jQuery plugin
  source: languages.ttAdapter(),
	templates: {
		empty: [
			'<div class="empty-message">',
			'unable to find any languages matching the current query',
			'</div>'
		].join('\n'),
		suggestion: Handlebars.compile('<p>{{name}} [{{code}}]</p>')
	}
});
