--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   23:09:39 10/12/2019
-- Design Name:   
-- Module Name:   C:/Users/jorilla/musicplayer/musicplayer/playertest.vhd
-- Project Name:  musicplayer
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: musicplayer
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY playertest IS
END playertest;
 
ARCHITECTURE behavior OF playertest IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT musicplayer
    PORT(
         clk : IN  std_logic;
         rst : IN  std_logic;
         addr : OUT  std_logic_vector(22 downto 0);
         swt : IN  std_logic_vector(7 downto 0);
         led : OUT  std_logic_vector(7 downto 0);			
			  disp : out std_logic_vector(3 downto 0);
			  seg : out std_logic_vector(6 downto 0);
         spk : inOUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal rst : std_logic := '0';
   signal swt : std_logic_vector(7 downto 0) := (others => '0');

 	--Outputs
   signal addr : std_logic_vector(22 downto 0);
   signal led : std_logic_vector(7 downto 0);
   signal spk : std_logic;

   -- clk period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: musicplayer PORT MAP (
          clk => clk,
          rst => rst,
          addr => addr,
          swt => swt,
          led => led,
          spk => spk
        );

   -- clk process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		wait for 20ns;
      rst <= '1';
		wait for 7ns;
		rst <= '0';

      -- insert stimulus here 

      wait;
   end process;

END;
