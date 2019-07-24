#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *


class TestSuite:

    def test(self):

        # VEX.256.66.0F38.W0 1A /r
        # VBROADCASTF128 ymm1, m128

        myVEX = VEX('VEX.256.66.0F38.W0')
        myVEX.vvvv = 0b1111
        Buffer = '{}1a20'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf128 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf128 ymm12, xmmword ptr [r8]')

        # EVEX.256.66.0F38.W0 1A /r
        # VBROADCASTF32X4 ymm1 {k1}{z}, m128

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}1a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf32x4 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf32x4 ymm4, xmmword ptr [rax]')

        # EVEX.512.66.0F38.W0 1A /r
        # VBROADCASTF32X4 zmm1 {k1}{z}, m128

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}1a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf32x4 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf32x4 zmm4, xmmword ptr [rax]')

        # EVEX.256.66.0F38.W1 1A /r
        # VBROADCASTF64X2 ymm1 {k1}{z}, m128

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}1a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf64x2 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf64x2 ymm4, xmmword ptr [rax]')

        # EVEX.512.66.0F38.W1 1A /r
        # VBROADCASTF64X2 zmm1 {k1}{z}, m128

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}1a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf64x2 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf64x2 zmm4, xmmword ptr [rax]')







        # VEX.256.66.0F38.W0 19 /r
        # VBROADCASTSD ymm1, m64

        myVEX = VEX('VEX.256.66.0F38.W0')
        myVEX.vvvv = 0b1111
        Buffer = '{}1920'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastsd ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastsd ymm12, qword ptr [r8]')

        # VEX.256.66.0F38.W0 19 /r
        # VBROADCASTSD ymm1, xmm2

        myVEX = VEX('VEX.256.66.0F38.W0')
        myVEX.vvvv = 0b1111
        Buffer = '{}19c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastsd ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastsd ymm8, xmm8')

        # EVEX.256.66.0F38.W1 19 /r
        # VBROADCASTSD ymm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}1920'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastsd ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastsd ymm4, qword ptr [rax]')

        # EVEX.512.66.0F38.W1 19 /r
        # VBROADCASTSD zmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}1920'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastsd ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastsd zmm4, qword ptr [rax]')

        # EVEX.256.66.0F38.W0 19 /r
        # VBROADCASTF32X2 ymm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}1920'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf32x2 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf32x2 ymm4, qword ptr [rax]')

        # EVEX.512.66.0F38.W0 19 /r
        # VBROADCASTF32X2 zmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}1920'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vbroadcastf32x2 ')
        assert_equal(myDisasm.instr.repr, 'vbroadcastf32x2 zmm4, qword ptr [rax]')