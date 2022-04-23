use std::fmt;

#[derive(Clone)]
struct TCount<T>
{
    pub t: T,
    pub num: u8,
}

impl<T> fmt::Display for TCount<T> 
where T: fmt::Display
{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self.num {
            1 => write!(f, "{}", self.t),
            _ => write!(f, "({})[{}]", self.t, self.num),
        }
    }
}

pub struct RunLengthEncoded<T> {
    elements: Vec<TCount<T>>,
}

impl<T> RunLengthEncoded<T> 
where T: PartialEq + Copy,
{
    pub fn encode(input: Vec<T>) -> Result<RunLengthEncoded<T>, &'static str> {
        if input.len() < 2 {
            return Err("input vector length is < 2")
        }

        let mut result = vec![TCount{t: input[0], num: 1}];
        let mut idx = 0;
        for t in input[1..].into_iter() {
            let mut current = &mut result[idx];

            if current.t == *t && current.num != 255 {
                current.num += 1;
            } else {
                result.push(TCount{t: *t, num: 1});
                idx += 1;
            }
        }

        Ok(RunLengthEncoded{elements: result})
    }
    
}

impl<T> fmt::Display for RunLengthEncoded<T>
where T: fmt::Display {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for elem in &self.elements {
            write!(f, "{}", elem)?;
        }
        write!(f, "")
    }
}