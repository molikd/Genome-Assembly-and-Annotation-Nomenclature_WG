import argparse
import re

# Constants
MAX_ID_NUMBER = 999999

# This pattern matches a valid genome assembly identifier as per the given guideline
VALID_ASSEMBLY_REGEX = re.compile(
    r'^([A-Za-z0-9]+)\.([A-Za-z0-9]+)\.([A-Za-z0-9]+)\.(\d+)\.(\d+)(\.([A-Za-z0-9]+))?\.fasta$'
)

# This pattern matches a valid gene model identifier as per the given guideline
VALID_GENE_MODEL_REGEX = re.compile(
    r'^([A-Za-z0-9]+)(g|p|pan|t)(\d{6})$'
)

# Assembly identifier template
ASSEMBLY_ID_TEMPLATE = "{tol_id}.{sample_identifier}.{consortium}.{version}.{subversion}{optional}.fasta"

# Gene model identifier template
GENE_MODEL_ID_TEMPLATE = "{assembly_prefix}{entity}{id_number}"

def create_assembly_identifier(tol_id, sample_identifier, consortium, version, subversion, optional=''):
    """Construct a valid assembly identifier based on the provided components."""
    # Ensure version and subversion are numbers
    version = int(version)
    subversion = int(subversion)

    return ASSEMBLY_ID_TEMPLATE.format(
        tol_id=tol_id,
        sample_identifier=sample_identifier,
        consortium=consortium,
        version=version,
        subversion=subversion,
        optional=f".{optional}" if optional else ""
    )

def validate_assembly_identifier(assembly_id):
    """Validate the given assembly identifier against the pattern."""
    return bool(VALID_ASSEMBLY_REGEX.match(assembly_id))

def create_gene_model_identifier(assembly_prefix, entity, id_number):
    """Construct a valid gene model identifier based on the provided components."""
    # Ensure id_number is an integer and within range
    id_number = int(id_number)
    if not 0 <= id_number <= MAX_ID_NUMBER:
        raise ValueError(f"ID number must be within 0 and {MAX_ID_NUMBER}")

    return GENE_MODEL_ID_TEMPLATE.format(
        assembly_prefix=assembly_prefix,
        entity=entity,
        id_number=str(id_number).zfill(6)  # Fill with zeros to ensure 6 digits
    )

def validate_gene_model_identifier(gene_model_id):
    """Validate the given gene model identifier against the pattern."""
    return bool(VALID_GENE_MODEL_REGEX.match(gene_model_id))

def main():
    parser = argparse.ArgumentParser(description="Genome Assembly and Gene Model Identifier Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Create assembly identifier
    parser_assembly = subparsers.add_parser('create-assembly', help='Create a genome assembly identifier')
    parser_assembly.add_argument('tol_id', type=str, help='Tree of Life Identifier')
    parser_assembly.add_argument('sample_identifier', type=str, help='Sample Identifier')
    parser_assembly.add_argument('consortium', type=str, help='Consortium/Project/Group')
    parser_assembly.add_argument('version', type=int, help='Assembly Version Number')
    parser_assembly.add_argument('subversion', type=int, help='Assembly Subversion Number')
    parser_assembly.add_argument('--optional', type=str, help='Optional Naming Component', default='')

    # Validate assembly identifier
    parser_validate_assembly = subparsers.add_parser('validate-assembly', help='Validate a genome assembly identifier')
    parser_validate_assembly.add_argument('assembly_id', type=str, help='Assembly Identifier to validate')

    # Create gene model identifier
    parser_gene_model = subparsers.add_parser('create-gene-model', help='Create a gene model identifier')
    parser_gene_model.add_argument('assembly_prefix', type=str, help='Assembly Prefix')
    parser_gene_model.add_argument('entity', type=str, help='Entity (e.g., g for gene)')
    parser_gene_model.add_argument('id_number', type=int, help='Unique Identifier Number')

    # Validate gene model identifier
    parser_validate_gene_model = subparsers.add_parser('validate-gene-model', help='Validate a gene model identifier')
    parser_validate_gene_model.add_argument('gene_model_id', type=str, help='Gene Model Identifier to validate')

    args = parser.parse_args()

    if args.command == 'create-assembly-name':
        assembly_id = create_assembly_identifier(
            args.tol_id,
            args.sample_identifier,
            args.consortium,
            args.version,
            args.subversion,
            args.optional
        )
        print(f"Generated Assembly Identifier: {assembly_id}")

    elif args.command == 'validate-assembly-name':
        is_valid = validate_assembly_identifier(args.assembly_id)
        print(f"Assembly Identifier Valid: {is_valid}")

    elif args.command == 'create-gene-model-name':
        gene_model_id = create_gene_model_identifier(
            args.assembly_prefix,
            args.entity,
            args.id_number
        )
        print(f"Generated Gene Model Identifier: {gene_model_id}")

    elif args.command == 'validate-gene-model-name':
        is_valid = validate_gene_model_identifier(args.gene_model_id)
        print(f"Gene Model Identifier Valid: {is_valid}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
