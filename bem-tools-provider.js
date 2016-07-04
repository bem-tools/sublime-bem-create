const bemToolsCreate = require('bem-tools-create')
const getStdin = require('get-stdin');
const fs = require('fs');
console.log('Node was started\n')

// Example enters data - [[{"block": "vitaly"}], [{"path": "C:/sublime/Data/Packages/BemTools"}], [{"techs": "['css', 'js']"}]]
getStdin().then(options => {
	const entitiesData = JSON.parse(options)
	const {block, paths, techs} = entitiesData;
	bemToolsCreate(block, paths, techs)
});
