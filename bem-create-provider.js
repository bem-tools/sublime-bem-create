'use strict';

const bemToolsCreate = require('bem-tools-create');
const getStdin = require('get-stdin');

getStdin().then(options => {
	const entitiesData = JSON.parse(options);
	bemToolsCreate(entitiesData.block, entitiesData.paths, entitiesData.techs);
});
