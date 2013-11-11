# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

"""
@brief Java language specific LOXI generating configuration

This language specific file defines:

target_files:  List of internal references to files to generate
file_gen_map: The map from above file references to generator functions
file_to_name_map: The map from internal references to external file names
file_to_subdir_map: The map from internal references to external subdirectories

HOWEVER, since java files are all a function of their class name, we don't
know in advance what the names of the files/classes will be, so we just
define a single directory and generate everything in there.
    @fixme talk to DanT to see if there isn't something that makes more sense

"""

import os
import loxi_utils.loxi_utils as loxi_utils
import java_gen.codegen as java_codegen


targets = {
    'openflowj/README': java_codegen.gen_all_java
}

def generate():
    for (name, fn) in targets.items():
        with loxi_utils.open_output(name) as outfile:
            fn(outfile, os.path.basename(name))
