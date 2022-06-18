/// Linear search.

pub fn linear_search<T>(arr: &[T], target: &T) -> Option<usize>
where
    T: PartialEq,
{
    for (index, item) in arr.iter().enumerate() {
        if item == target {
            return Some(index);
        }
    }
    None
}
