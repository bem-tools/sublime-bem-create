const bemToolsCreate = require('bem-tools-create')
const getStdin = require('get-stdin');

getStdin().then(options => {
	const entitiesData = JSON.parse(options)
	const {block, paths, techs} = entitiesData;
	bemToolsCreate(block, paths, techs)
});
