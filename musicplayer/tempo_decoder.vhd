----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    22:51:36 10/03/2019 
-- Design Name: 
-- Module Name:    beat_decoder - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity tempo_decoder is
    Port ( tempo : in  STD_LOGIC_VECTOR (6 downto 0);
           beat_len : out  STD_LOGIC_VECTOR (27 downto 0));
end tempo_decoder;

architecture Behavioral of tempo_decoder is

begin
	-- theres probably a better way to do this by adding onto a base beat value
	-- but whatever

	beat_len <= X"17d7840" when tempo = "0111100" else
					X"1773753" when tempo = "0111101" else
					X"1712a0c" when tempo = "0111110" else
					X"16b4df3" when tempo = "0111111" else
					X"165a0bc" when tempo = "1000000" else
					X"160203b" when tempo = "1000001" else
					X"15aca68" when tempo = "1000010" else
					X"1559d5b" when tempo = "1000011" else
					X"1509747" when tempo = "1000100" else
					X"14bb67a" when tempo = "1000101" else
					X"146f95b" when tempo = "1000110" else
					X"1425e68" when tempo = "1000111" else
					X"13de435" when tempo = "1001000" else
					X"1398969" when tempo = "1001001" else
					X"1354cbe" when tempo = "1001010" else
					X"1312d00" when tempo = "1001011" else
					X"12d290a" when tempo = "1001100" else
					X"1293fc7" when tempo = "1001101" else
					X"1257031" when tempo = "1001110" else
					X"121b94d" when tempo = "1001111" else
					X"11e1a30" when tempo = "1010000" else
					X"11a91f6" when tempo = "1010001" else
					X"1171fca" when tempo = "1010010" else
					X"113c2e1" when tempo = "1010011" else
					X"1107a76" when tempo = "1010100" else
					X"10d45d2" when tempo = "1010101" else
					X"10a2444" when tempo = "1010110" else
					X"1071523" when tempo = "1010111" else
					X"10417ce" when tempo = "1011000" else
					X"1012bac" when tempo = "1011001" else
					X"0fe502a" when tempo = "1011010" else
					X"0fb84bc" when tempo = "1011011" else
					X"0f8c8db" when tempo = "1011100" else
					X"0f61c08" when tempo = "1011101" else
					X"0f37dc6" when tempo = "1011110" else
					X"0f0eda1" when tempo = "1011111" else
					X"0ee6b28" when tempo = "1100000" else
					X"0ebf5ed" when tempo = "1100001" else
					X"0e98d8a" when tempo = "1100010" else
					X"0e7319b" when tempo = "1100011" else
					X"0e4e1c0" when tempo = "1100100" else
					X"0e29d9d" when tempo = "1100101" else
					X"0e064da" when tempo = "1100110" else
					X"0de3722" when tempo = "1100111" else
					X"0dc1424" when tempo = "1101000" else
					X"0d9fb92" when tempo = "1101001" else
					X"0d7ed1f" when tempo = "1101010" else
					X"0d5e883" when tempo = "1101011" else
					X"0d3ed78" when tempo = "1101100" else
					X"0d1fbbb" when tempo = "1101101" else
					X"0d0130b" when tempo = "1101110" else
					X"0ce3329" when tempo = "1101111" else
					X"0cc5bd9" when tempo = "1110000" else
					X"0ca8ce0" when tempo = "1110001" else
					X"0c8c606" when tempo = "1110010" else
					X"0c70716" when tempo = "1110011" else
					X"0c54fda" when tempo = "1110100" else
					X"0c3a020" when tempo = "1110101" else
					X"0c1f7b8" when tempo = "1110110" else
					X"0c05672" when tempo = "1110111" else
					X"0bebc20" when tempo = "1111000";


end Behavioral;

