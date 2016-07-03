const bemToolsCreate = require('bem-tools-create')
const getStdin = require('get-stdin');
const fs = require('fs');

// bemToolsCreate([[{"block": "vitaly"}], [{"path": "C:/sublime/Data/Packages/BemTools"}], [{"techs": "['css', 'js']"}]]);
getStdin().then(options => {
	const obj = JSON.parse(options)
	const {block, paths, techs} = obj;
	bemToolsCreate(block, paths, techs)

});


// 	const {blocks, paths, techs} = options;


//[
//     { block: 'vitaly-harisov' },
//     { block: 'vitaly-harisov', modName: 'm1', modVal: true },
//     { block: 'vitaly', elem: 'e2' },
//     { block: 'vitaly', elem: 'e2', modName: 'elemMod', modVal: true },
//     { block: 'harisov', modName: 'm1', modVal: 'v1' }
// ], ['tmp', 'tmp2', 'path/to/level'], ['css', 'js', 'bemhtml.js']
