
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


class VEX:
    def __init__(self):
        self.reset()

    def reset(self):
        self.L = 0
        self.pp = 0
        self.mmmm = 0
        self.W = 0
        self.vvvv = 0
        self.R = 0
        self.X = 0
        self.B = 0

    def byte1(self):
        return self.mmmm + (self.B << 5) + (self.X << 6) + (self.R << 7)

    def byte2(self):
        return self.pp + (self.L << 2) + (self.vvvv << 3) + (self.W << 7)


class TestSuite:
    def test(self):

        # VEX.NDS.128.66.0F38.W0 96 /r
        # vfmaddsub132ps xmm1, xmm2, xmm3/m128
        Buffer = 'c4020196443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132ps ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132ps xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.W0 96 /r
        # vfmaddsub132ps ymm1, ymm2, ymm3/m256
        Buffer = 'c4020596443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132ps ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132ps ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F38.W0 96 /r
        # vfmaddsub132ps xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '6202050696443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x96')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132ps ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132ps xmm0, xmm15, xmmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.256.66.0F38.W0 96 /r
        # vfmaddsub132ps ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '6202052096443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x96')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132ps ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132ps ymm0, ymm15, ymmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.512.66.0F38.W0 96 /r
        # vfmaddsub132ps zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '6202054096443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x96')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132ps ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132ps zmm0, zmm15, zmmword ptr [rbx+rsi+22h]')


        # VEX.NDS.128.66.0F38.W1 96 /r
        # vfmaddsub132pd xmm1, xmm2, xmm3/m128

        myVEX = VEX()
        myVEX.L = 0
        myVEX.W = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b0

        Buffer = 'c4{:02x}{:02x}96443322'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmaddsub132pd ')
        assert_equal(myDisasm.instr.repr, 'vfmaddsub132pd xmm8, xmm15, xmmword ptr [r11+r14+22h]')


