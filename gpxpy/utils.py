# -*- coding: utf-8 -*-

# Copyright 2011 Tomo Krajina
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

def to_cdata( str ):
	if not str:
		return '<![CDATA[]]>'
	return '<![CDATA[%s]]>' % str.replace( ']]>', '???' )

def to_xml( tag, attributes = {}, content = None, cdata = None ):
	result = '\n<%s' % tag
	if attributes:
		for attribute in attributes.keys():
			result += ' %s="%s"' % ( attribute, attributes[ attribute ] )
	if content:
		if cdata:
			result += '>%s</%s>' % ( to_cdata( content ), tag )
		else:
			result += '>%s</%s>' % ( content, tag )
	else:
		result += ' />'

	result += ''

	if isinstance( result, unicode ):
		result = result.encode( 'utf-8' )
	
	return result

def to_number( str, default = 0 ):
	if not str:
		return None
	return float( str )

def find_first_node( node, child_node_name ):
	if not node or not child_node_name:
		return None
	child_nodes = node.childNodes
	for child_node in child_nodes:
		if child_node.nodeName == child_node_name:
			return child_node
	return None

# Hash utilities:

def __hash( obj ):
	result = 0

	if obj == None:
		return result
	elif isinstance( obj, dict ):
		raise Error( '__hash_single_object for dict not yet implemented' )
	elif isinstance( obj, list ) or isinstance( obj, tuple ):
		return hash_list_or_tuple( obj )

	return hash( obj )

def hash_list_or_tuple( iteration ):
	result = 17

	for obj in iteration:
		result = result * 31 + __hash( obj )

	return result

def hash_object( obj, *attributes ):
	result = 19

	for attribute in attributes:
		result = result * 31 + __hash( getattr( obj, attribute ) )
	
	return result

