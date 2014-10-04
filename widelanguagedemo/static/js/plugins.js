// place any jQuery/helper plugins in here, instead of separate, slower script files.

var languages = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  limit: 10,
  prefetch: {
    // url points to a json file that contains an array of country names, see
    // https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
    url: '/languages.json',
    // the json file contains an array of strings, but the Bloodhound
    // suggestion engine expects JavaScript objects so this converts all of
    // those strings
    filter: function(list) {
      return $.map(list, function(language) { return { name: language }; });
    }
  }
});

// kicks off the loading/processing of `local` and `prefetch`
languages.initialize();

// passing in `null` for the `options` arguments will result in the default
// options being used
$('#prefetch .typeahead').typeahead(null, {
  name: 'languages',
  displayKey: 'name',
  // `ttAdapter` wraps the suggestion engine in an adapter that
  // is compatible with the typeahead jQuery plugin
  source: languages.ttAdapter()
});
