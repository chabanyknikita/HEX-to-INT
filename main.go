package main

import (
	"encoding/binary"
	"encoding/hex"
	"fmt"
	"math/big"
	"strings"
)

func hex_to_big_endian(s string) *big.Int {
	numberStr := strings.Replace(s, "0x", "", -1)
	numberStr = strings.Replace(numberStr, "0X", "", -1)
	n := new(big.Int)
	n.SetString(numberStr, 16)
	return n
}
func hex_to_little_endian(s string) uint32 {
	numberStr := strings.Replace(s, "0x", "", -1)
	numberStr = strings.Replace(numberStr, "0X", "", -1)
	decodedByteArray, err := hex.DecodeString(numberStr)

	if err != nil {
		fmt.Println("Unable to convert hex to byte. ", err)
	}
	data := binary.LittleEndian.Uint32(decodedByteArray)
	return data
}
func print_all() {
	var str string
	fmt.Println("Write value:")
	fmt.Scan(&str)
	fmt.Println("Value: ", str)
	numberStr := strings.Replace(str, "0x", "", -1)
	numberStr = strings.Replace(numberStr, "0X", "", -1)
	size := (len(numberStr) / 2)
	fmt.Println("Number of bytes: ", size)
	fmt.Println("Little-endian: ", hex_to_little_endian(str))
	fmt.Println("Big-endian: ", hex_to_big_endian(str))
	
	h := fmt.Sprintf("%x", hex_to_little_endian(str))
	k := fmt.Sprintf("%x", hex_to_little_endian(str))
	fmt.Printf("Little-endian: %d to HEX: 0x%s\n", hex_to_little_endian(str), h)
	fmt.Printf("Big-endian: %d to HEX 0x%s", hex_to_big_endian(str), k)

}

func main() {
	print_all()
}
