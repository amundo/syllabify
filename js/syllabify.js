function assemblePattern(text){
  var letters = $.trim(text).split(/[ ]+/);

  var sortedLetters = _.sortBy(letters, function(w){ 
    return -w.length;
  })

  return '(' + sortedLetters.join('|') + ')';
}

function phonemicize(word, pattern){
  var word = $.trim(word).toLowerCase();
  var re = new RegExp(pattern, 'g');
  return word.match(re);
}

function tokenize(text){
  return $.trim(text).split(/[\. \,\n]+/); 
}

function syllabify(phonemes){
  return  phonemes;
}

$(function(){

var text = $('textarea#wordList').val();
var words = tokenize(text);
var template = _.template($('#wordTemplate').html());

$.each(words, function(i,spelling){
  $('#words').append(template({spelling: spelling}));
})

function syllabifyAll(ev){
console.log(ev.which);

  $('ol.word').each(function(i, ol){
  
    var spelling = $(ol).find('li.spelling').text();
    var $phonemes = $(ol).find('li.phonemes');

    var pattern = assemblePattern($('#alphabet').val());

    var phonemes = phonemicize(spelling, pattern);
console.log(spelling,phonemes);
    $phonemes.html(phonemes.join('<span style="color:#cecece;margin: 0 4px">|</span>'));

  })

}
//·

$('#alphabet').on('keyup', syllabifyAll );

})
