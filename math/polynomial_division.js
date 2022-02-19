import {Addend} from "./Addend";

class Addend {
    constructor(addend_string){
        this.addend = String(addend_string).split('x^');
        this.coefficient = parseInt(this.addend[0]);
        this.degree = parseInt(this.addend[1]);
    }
}

function complete(arr) {
    const res =  arr
        .sort((a,b) => b.degree - a.degree)
        .reduce((acc, curr, idx, arr) => {
            while (acc.length && acc[acc.length-1].degree - curr.degree !== 1) {
                acc.push(new Addend(`0x^${acc[acc.length-1].degree - 1}`));
            }
            acc.push(curr);
            return acc;
        }, []);
    while (res[res.length-1].degree > 0) {
        res.push(new Addend(`0x^${res[res.length-1].degree - 1}`));
    }
    return res;
}

export function calculate(nu, de, rep=false){
    console.log("\nCALC");
    console.log(nu);
    console.log(de);

    de = complete(de);

    let poly = complete(nu);
    const res = [];
    while (poly.length) {
        // division
        const quot = division(poly[0], de[0], false);
        console.log('quot', quot);
        res.push(quot);

        // multiplication
        const prod = multiplication(quot, de, false);
        console.log('prod', prod);

        // subtraction (prod - poly)
        const degs = [...prod, ...poly].map(x => x.degree);
        const mx_deg = Math.max(...degs);
        const mn_deg = Math.min(...degs);
        const diff = [];
        for (let deg = mx_deg; deg >= mn_deg; deg--) {
            const minuend = poly.find(x => x.degree === deg) || new Addend(`0x^${deg}`);
            const subtrahend = prod.find(x => x.degree === deg) || new Addend(`0x^${deg}`);
            diff.push(subtraction(minuend, subtrahend, false));
        }
        console.log('diff', diff);
        poly = diff.filter(x => x.coefficient !== 0);
    }

    console.log('res', res);
    return res;
}


export function division(dividendTerm, divisorTerm, dd=true){
    dd && console.log("\nDIVISION");
    dd && console.log(dividendTerm);
    dd && console.log(divisorTerm);

    const D = dividendTerm.degree - divisorTerm.degree;
    const C = dividendTerm.coefficient / divisorTerm.coefficient;
    const res = `${C}x^${D}`;
    dd && console.log('res', res);

    return new Addend(res);
}


export function multiplication(f1, ff2, dd=true){
    dd && console.log("\nMULTIPLICATION");
    dd && console.log(f1);
    dd && console.log(ff2);

    return ff2.map(f => {
        const C = f1.coefficient*f.coefficient;
        const D = f1.degree+f.degree;
        const res = `${C}x^${D}`;
        dd && console.log('res', res);
        return new Addend(res);
    });
}


export function subtraction(minuend, subtrahend, dd=true){
    dd && console.log("\nSUBTRACTION");
    dd && console.log(minuend);
    dd && console.log(subtrahend);

    const C = minuend.coefficient - subtrahend.coefficient;
    const D = minuend.degree;
    const res = `${C}x^${D}`;
    dd && console.log('res', res);

    return new Addend(res);
}
