use std::fmt;

#[derive(Clone)]
struct ByteCount {
    pub byte: u8,
    pub num: u32,
}

impl ByteCount {
    pub fn new(byte: u8, num: u32) -> ByteCount {
        ByteCount {
            byte, num
        }
    }
}

impl fmt::Display for ByteCount {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self.num {
            0 => write!(f, "{}", self.byte),
            _ => write!(f, "{}[{}]", self.byte, self.num),
        }
    }
}

pub struct RunLengthEncoded {
    elements: Vec<ByteCount>,
}

impl RunLengthEncoded {
    pub fn encode(string: &str) -> RunLengthEncoded {
        let mut result = vec![ByteCount::new(0, 0)];
        let mut idx = 0;
        for by in string.bytes() {
            let mut current = &mut result[idx];
            if current.byte == by {
                current.num += 1;
            } else {
                result.push(ByteCount::new(by, 1));
                idx += 1;
            }
            
        }

        match result[0].byte {
            0 => RunLengthEncoded{elements: result[1..].to_vec()},
            _ => RunLengthEncoded{elements: result}
        }
    }
}

impl fmt::Display for RunLengthEncoded {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for elem in &self.elements {
            write!(f, "{} ", elem)?;
        }
        write!(f, "")
    }
}